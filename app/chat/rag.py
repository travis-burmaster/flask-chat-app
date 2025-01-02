from supabase import create_client
from vertexai.language_models import TextGenerationModel
from vertexai.language_models import TextEmbeddingModel
from app.config import Config

class RAGChat:
    def __init__(self):
        self.supabase = create_client(Config.SUPABASE_URL, Config.SUPABASE_KEY)
        self.llm = TextGenerationModel.from_pretrained('gemini-1.5-flash')
        self.embedding_model = TextEmbeddingModel.from_pretrained('text-embedding-004')

    def get_embeddings(self, text):
        embedding = self.embedding_model.get_embeddings([text])[0]
        return embedding.values

    def search_documents(self, query_embedding):
        response = self.supabase.rpc(
            'match_documents',
            {'query_embedding': query_embedding, 'match_count': 3}
        ).execute()
        return response.data

    def get_response(self, query):
        query_embedding = self.get_embeddings(query)
        relevant_docs = self.search_documents(query_embedding)
        
        context = ' '.join([doc['content'] for doc in relevant_docs])
        prompt = f"Context: {context}\n\nQuestion: {query}\n\nAnswer:"
        
        response = self.llm.predict(prompt)
        return response.text