class temp :
    @staticmethod
    def celsius_to_farninte(celcius):
        return (celcius*9/5)+32
    @staticmethod
    def farnite_to_celsius(farnite):
        return(farnite-32)*5/9
    @staticmethod
    def celsius_to_kalvin(celsius):
        return celsius+273.15
    @staticmethod
    def farnite_to_kalvine(farnite):
        celsius = temp.farnite_to_celsius(farnite)
        return temp.celsius_to_kalvin(celsius)
    
if __name__ == "__main__":
    f = temp.celsius_to_farninte(100)
    c  = temp.farnite_to_celsius(37)
    k = temp.farnite_to_kalvine(70)
    print(f,c,k)
    
    