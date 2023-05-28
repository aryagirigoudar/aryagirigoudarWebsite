import requests as req

from datetime import date



API_KEY = "3cf14f378fmshf5b0697e38b0df3p1f17d6jsne78505db628e"
API_HOST = "alpha-vantage.p.rapidapi.com"




class get_from_my_profiles:
    def get_data():
        """
            Function returns dictionary of titles:description of my github profile ( Only public repos )
        """
        json_data = req.get("https://api.github.com/users/aryagirigoudar/repos").json()

        dataindict = {}
        for index in range(len(json_data)):
            dataindict[json_data[index]["name"]] = json_data[index]["description"]
        return dataindict


class data:
    """
        Function to get all kind of data shown in my website
    """
    def get_stock_data_alpha_vantage():
        

        url = "https://alpha-vantage.p.rapidapi.com/query"

        querystring = {"function":"TIME_SERIES_DAILY","symbol":"INFY.BSE","datatype":"json","outputsize":"compact"}

        headers = {
            "X-RapidAPI-Key": API_KEY,
            "X-RapidAPI-Host": API_HOST
        }

        response = req.get(url, headers=headers, params=querystring)

        f = open("output.op","w+")
        f.writelines(str(response.json()))
        
        f.close()
    
    def get_stock_data_nsepy():
        # data = get_history(symbol="INFY",  start=date(2020,1,1), end=date(2023,1,31))
        # data[['Close']].plot()
        import investpy

        df = investpy.get_stock_historical_data(stock='AAPL',
                                                country='United States',
                                                from_date='01/01/2010',
                                                to_date='01/01/2020')
        print(df)

data.get_stock_data_alpha_vantage()


