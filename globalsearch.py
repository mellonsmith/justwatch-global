from justwatch import JustWatch
searchcountrys = ['US', 'GB', 'DE', 'FR', 'CA', 'AU', 'NZ', 'IN', 'IT', 'ES', 'BR', 'MX']
#searchcountrys = ['US']
def get_streaming_providers(title, mycountry):
    # Search for the title
    just_watch = JustWatch(country=mycountry)
    results = just_watch.search_for_item(query=title)
    # Get the streaming providers
    streaming_providers = []
    for provider in results['items'][0]['offers']:
        if provider['monetization_type'] == 'flatrate':
            provider_dict = [
                provider['package_short_name'],
                provider['urls']['standard_web']
                ]
            streaming_providers.append(provider_dict)
    return streaming_providers

def main():
    title = input("Enter the title of the movie or TV show: ")
    print("Searching for streaming providers...")
    for country in searchcountrys:
        streaming_providers = get_streaming_providers(title, country)
        print(country + ": " + str(streaming_providers) + "\n")

if __name__ == '__main__':
    main()