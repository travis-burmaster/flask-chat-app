# Flask RAG Chat Application

A Flask-based RAG (Retrieval-Augmented Generation) chat application using:
- Office 365 authentication
- Supabase vector store
- Vertex AI (Gemini 1.5 Flash and Text Embedding 004)

## Setup

1. Clone the repository
2. Copy `.env.example` to `.env` and fill in your credentials
3. Install dependencies: `pip install -r requirements.txt`
4. Run the application: `python run.py`

## Configuration

### Required Environment Variables:
- Azure AD credentials (for O365 auth)
- Supabase credentials
- Google Cloud credentials

## Development

See individual components in the `/app` directory:
- `/auth`: Office 365 authentication
- `/chat`: RAG implementation
- `/templates`: Frontend views

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt 