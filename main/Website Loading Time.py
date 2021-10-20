from urllib.request import urlopen
import time


def get_load_time(url):
    """This function takes a user defined url as input
    and returns the time taken to load that url in seconds.
    Args:
        url (string): The user defined url.
    Returns:
        time_to_load (float): The time taken to load the website in seconds.
        Please enter a correct url (string): Ask the user to re-enter a correct url.
    """
    if '.' not in url:  # Checking if the url does not contains dot
        return "Please enter a correct url"
    if ("https" or "http") in url:  # Checking for presence of protocols
        open_the_url = urlopen(url)  # Open the url as entered by the user
    else:
        open_the_url = urlopen("https://" + url)  # Adding https to the url
    start_time = time.time()  # Time stamp before the reading of url starts
    open_the_url.read()  # Reading the user defined url
    end_time = time.time()  # Time stamp after the reading of the url
    open_the_url.close()  # Closing the instance of the urlopen object
    time_to_load = end_time - start_time

    return time_to_load


if __name__ == "__main__":
    url = input("Please enter the url you want to check it's loading time : ")
    load_time = get_load_time(url)
    if type(load_time) == float:    # Checking if the load time type is float
        print(f"The time taken to load {url} is {load_time:.2}")
    else:
        print(load_time)
