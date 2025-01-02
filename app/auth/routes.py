from flask import redirect, url_for, session, request
from flask_login import login_user, logout_user, current_user
from . import bp
from ..models import User
import msal

@bp.route('/login')
def login():
    if not session.get('flow', {}):
        flow = msal.ConfidentialClientApplication(
            Config.AZURE_CLIENT_ID,
            authority=f'https://login.microsoftonline.com/{Config.AZURE_TENANT_ID}',
            client_credential=Config.AZURE_CLIENT_SECRET
        )
        auth_url = flow.get_authorization_request_url(
            scopes=['User.Read'],
            redirect_uri=url_for('auth.authorized', _external=True)
        )
        session['flow'] = flow.serialize()
        return redirect(auth_url)
    return redirect(url_for('chat.index'))

@bp.route('/authorized')
def authorized():
    flow = msal.ConfidentialClientApplication.deserialize(session['flow'])
    result = flow.acquire_token_by_authorization_code(
        request.args['code'],
        scopes=['User.Read'],
        redirect_uri=url_for('auth.authorized', _external=True)
    )
    if 'error' in result:
        return redirect(url_for('auth.login'))
    user = User.get_or_create(result)
    login_user(user)
    return redirect(url_for('chat.index'))

@bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.login'))