from unittest.mock import patch


def test_get_retriever_uses_k():
    with patch("app.retrieval.retriever.load_vectorstore") as mocked_loader:
        mocked_loader.return_value.as_retriever.return_value = "retriever"
        from app.retrieval.retriever import get_retriever

        output = get_retriever(k=7)
        assert output == "retriever"
        mocked_loader.return_value.as_retriever.assert_called_once()


def test_similarity_search_with_scores_format():
    with patch("app.retrieval.retriever.load_vectorstore") as mocked_loader:
        mocked_loader.return_value.similarity_search_with_score.return_value = [("doc", 0.1)]
        from app.retrieval.retriever import similarity_search_with_scores

        results = similarity_search_with_scores("diabetes", k=3)
        assert isinstance(results, list)
        assert len(results) == 1
