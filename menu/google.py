from googlesearch import search

def perform_google_search(query, num_results=10):
    try:
        # Perform the search and print the results
        for result in search(query, num=num_results, stop=num_results, pause=2):
            print(result)
    except Exception as e:
        print(f"An error occurred: {e}")

# Prompt the user for the search query
query = input("Enter your search query: ")

# Call the function to perform the search
perform_google_search(query)
