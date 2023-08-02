from justwatch import JustWatch
import prettytable
searchcountrys = ['US', 'GB', 'DE', 'FR', 'CA', 'AU', 'NZ', 'IN', 'IT', 'ES', 'BR', 'MX']   # List of countries to search for streaming providers

def get_streaming_providers(title, mycountry):
    just_watch = JustWatch(country=mycountry)
    results = just_watch.search_for_item(query=title)
    streaming_providers = []
    if (len(results['items']) != 0):                                
        if 'offers' in results['items'][0]:                         # Prevents error if Movie was found but has no streaming options
            for provider in results['items'][0]['offers']:
                if provider['monetization_type'] == 'flatrate':     # Only include providers that offer a flatrate subscription
                    provider_dict = [
                        provider['package_short_name'],
                        provider['urls']['standard_web']
                        ]
                    streaming_providers.append(provider_dict)
    return streaming_providers 

def main():
    title = input("Enter the title of the movie or TV show: ")
    print("Searching for streaming providers...")
    found = False                                                   # Prevents error if Movie is not existing
    for country in searchcountrys:
        streaming_providers = get_streaming_providers(title, country)
        if len(streaming_providers) != 0:
            streaming_providers = list(set(tuple(provider) for provider in streaming_providers))    # Remove duplicates
            print("Found {} streaming providers in {}:".format(len(streaming_providers), country))
            mytable = prettytable.PrettyTable()
            mytable.field_names = ["Provider", "URL"]
            for provider in streaming_providers:
                mytable.add_row([provider[0], provider[1]])
            print(mytable)
            print("\n")
            found = True
    if not found : 
        print(f"No streaming services were found that stream {title}.")

if __name__ == '__main__':
    main()