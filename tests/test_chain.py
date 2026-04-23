from unittest.mock import patch


def test_build_rag_chain_returns_chain():
    with patch("app.generation.chain.get_llm") as mocked_llm, patch(
        "app.generation.chain.get_retriever"
    ) as mocked_retriever, patch("app.generation.chain.RetrievalQA.from_chain_type") as mocked_factory:
        mocked_llm.return_value = "llm"
        mocked_retriever.return_value = "retriever"
        mocked_factory.return_value = "chain"

        from app.generation.chain import build_rag_chain

        chain = build_rag_chain(top_k=5, temperature=0.2)
        assert chain == "chain"


def test_build_summarize_chain_returns_chain():
    with patch("app.generation.chain.get_llm") as mocked_llm, patch("app.generation.chain.LLMChain") as mocked_chain:
        mocked_llm.return_value = "llm"
        mocked_chain.return_value = "summary_chain"

        from app.generation.chain import build_summarize_chain

        chain = build_summarize_chain(temperature=0.3)
        assert chain == "summary_chain"
