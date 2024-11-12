from tavily import TavilyClient

def tavily_search(query: str, api_key: str):
    """Perform a web search using the Tavily API.
    
    Args:
        query (str): The search query
        api_key (str): Tavily API key
    
    Returns:
        dict: The search results from Tavily
    """
    try:
        client = TavilyClient(api_key=api_key)
        response = client.qna_search(query=query, search_depth="advanced")
        return response
    except Exception as e:
        return f"Error performing search: {str(e)}"