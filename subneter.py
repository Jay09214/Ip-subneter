
from sys import prefix
'''
              __                      __                   
             /\ \                    /\ \__                
  ____  __  _\ \ \____    ___      __\ \ ,_\    __   _ __  
 /',__\/\ \/\ \ \ '__`\ /' _ `\  /'__`\ \ \/  /'__`\/\`'__\
/\__, `\ \ \_\ \ \ \L\ \/\ \/\ \/\  __/\ \ \_/\  __/\ \ \/ 
\/\____/\ \____/\ \_,__/\ \_\ \_\ \____\\ \__\ \____\\ \_\ 
 \/___/  \/___/  \/___/  \/_/\/_/\/____/ \/__/\/____/ \/_/ 

 I made it in holiday


'''


class subnetting_tool():
    def __init__(self, prefix):
        self.__prefix = prefix
        self.__subnet_lis = [[0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0]]

    def getPrefix(self):
        return self.__prefix

    def getSubnet_lis(self):
        return self.__subnet_lis

class Subnet_Prefix_Converter(subnetting_tool):
    def __init__(self, prefix):
        super().__init__(prefix)
        self.__result_lis = self.getSubnet_lis()
        self.__reversed_bin_lis = []
        self.__bin_string_lis = []
        self.prefix_convertion()
        self.lis_reverse() 
        self.binary_convertion()

    def prefix_convertion(self):
        limit = 0
        i = 0
        k = 0
        while i < len(self.getSubnet_lis()):
            while k < len(self.getSubnet_lis()[i]):
                self.__result_lis[i][k] = 1
                k += 1
                limit += 1
                if limit == self.getPrefix():
                    return self.__result_lis
            k = 0
            i += 1
    
    def lis_reverse(self):
        reversed_lis = []
        reversed_bin_lis = []
        for i in self.__result_lis:
            index2 = len(i)-1
            while index2 >= 0:
                reversed_bin_lis.append(i[index2])
                index2-=1
            reversed_lis.append(reversed_bin_lis)
            reversed_bin_lis = [] 
        self.__reversed_bin_lis = reversed_lis
        return(self.__reversed_bin_lis)

    def binary_convertion(self):
        power = 0
        index1 = 0
        index2 = 0
        res = 0
        result = ''
        limit = 0
        while index1 < len(self.__reversed_bin_lis):
            while index2 < len(self.__reversed_bin_lis[index1]):
                res += int(self.__reversed_bin_lis[index1][index2]) * 2**power
                index2 += 1
                power += 1
            index2 = 0
            power = 0
            result = result + str(res)
            if limit != len(self.__reversed_bin_lis)-1:

                limit+=1
                result += '.'
            res = 0
            index1+=1
        self.__result = result
        return self.__result

    def getResult(self):
        return self.__result

    def __str__(self):
        return str(self.__result)

    def __repr__(self):
        self.__str__()

class Host_calculator(subnetting_tool):
    def __init__(self, subnet):
        super().__init__(prefix)
        self.__subnet = subnet
        self.__num_lis = []
        self.__bin_lis = []
        self.__result = ''
        self.__total_host = 0
        self.integer_transform()
        self.decimal_trasnform()
        self.count_host()

    def getTotal_host(self):
        return self.__total_host

    def getResult(self):
        return self.__result
    
    def integer_transform(self):
        bin_lis = str(self.__subnet).split('.')
        self.__num_lis = bin_lis
        return self.__num_lis

    def decimal_trasnform(self):
        bin = ''
        j = 0
        k = 0
        res_lis = self.getSubnet_lis()

        for i in self.__num_lis:
            while (int(i)) > 0:
                bin = str(int(i)%2)
                i = int(i) // 2
                res_lis[j][k] = int(bin)
                k+=1
            j+=1
            k=0
        
        self.__bin_lis = res_lis
        return self.__bin_lis
    
    def count_host(self):
        index1 = 0
        index2 = 0
        power = 0
        available_host = 0
        while index1 < len(self.__bin_lis):
            while index2 < len(self.__bin_lis[index1]):
                if self.__bin_lis[index1][index2] == 0:
                    power += 1
                index2+=1
            index1+=1
            index2 = 0

        self.__total_host = 2 ** power
        available_host = self.__total_host - 2
        self.__result = available_host
        return self.__result

    def __str__(self):
        return str(self.__result)

    def __repr__(self):
        self.__str__()

class subnet_prediction(subnetting_tool):
    def __init__(self, host):
        super().__init__(prefix)
        self.__host = host
   
        self.__host_lis = []
        self.__subnet_lis = []
        self.__result = ''
        self.__result_host = 0
        self.calculate_total_host()
        self.find_subnet()

    def calculate_total_host(self):
        prefix = 1
        while prefix != 31:
            subnet_calculate = Subnet_Prefix_Converter(prefix)
            host = Host_calculator(subnet_calculate)
            self.__subnet_lis.append(subnet_calculate.getResult())
            self.__host_lis.append(host.getResult())
            prefix += 1

    def find_subnet(self):
        index = 0
        index2 = 0
        predict_lis = []
        result_index = 0
        while index < len(self.__host_lis):
            if self.__host_lis[index] >= self.__host:
                predict_lis.append(self.__host_lis[index])
            index += 1
        self.__result_host = predict_lis[len(predict_lis)- 1]
        
        for i in self.__host_lis:
            if i == self.__result_host:
                result_index = self.__host_lis.index(i)
        
        while index2 < len(self.__subnet_lis):
            if self.__subnet_lis.index(self.__subnet_lis[index2]) == result_index:
                self.__result = self.__subnet_lis[index2]
                return self.__result
            else:
                index2 += 1        

    def getResult_host(self):
        return self.__result_host

    def __str__(self):
        return self.__result

    def __repr__(self):
        self.__str__()


class VLSM_calculation():
    def __init__(self, IP_address, prefix):
        self.__IP_address = IP_address
        self.__prefix = prefix
        self.__host_prefix = 0
        self.__address_lis = [0,0,0,0]
        self.__host = 0
        self.__result_str = ''
        self.calculate_subnet()
        self.VLSM()

    def getHost(self):
        return self.__host

    def calculate_subnet(self):
        subnet = Subnet_Prefix_Converter(self.__prefix)
        self.__host = Host_calculator(subnet)

        subnet_lis = str(subnet).split('.')
        for i in subnet_lis:
            if i != '255':
                self.__host_prefix = subnet_lis.index(i)
                return self.__host_prefix

    def VLSM(self):
        address_lis = str(self.__IP_address).split('.')
        index = 0
        limit = 0
        while index < len(address_lis):
            self.__address_lis[index] = int(address_lis[index])
            index+=1
        
        count = 1
        self.__host = self.__host.getTotal_host()
        while count < self.__host:
            if count < self.__host:
                self.__address_lis[3] += 1
                count+=1
            if self.__address_lis[3] == 255 and count < self.__host:
                self.__address_lis[2] += 1
                self.__address_lis[3] = 0
                count+=1
                
            if self.__address_lis[2] == 255 and count < self.__host:
                self.__address_lis[1] += 1
                self.__address_lis[2] = 0
                count+=1
            if self.__address_lis[1] == 255 and count < self.__host:
                self.__address_lis[0] += 1
                self.__address_lis[1] = 0
                count+=1
            if self.__address_lis[0] == 255 and count < self.__host:
                return self.__address_lis
        print(self.__address_lis)


    def getResult(self):
        return self.__result_str


    def __str__(self):
        return self.__result_str

    def __repr__(self):
        self.__str__()


def main():
    run = True
    while run:
        start = print(
                    '\nsubnet option\n'
                    '1. subnet calculation\n'
                    '2. host calculation\n'
                    '3. simple VLSM (half complete)'
                )
        try:
            option = int(input('select your option: '))
            if option == 1:
                prefix = int(input('prefix (/): '))
                while prefix > 31:
                    print('the input is overwhelm and too little')
                    prefix = int(input('prefix (/): '))
                subnet = Subnet_Prefix_Converter(prefix)
                host = Host_calculator(subnet)
                print(f'the subnet is: {subnet}')
                print(f'total host has: {host.getTotal_host()}')
                print(f'available host has: {host}')

            elif option == 2:
                host = int(input('host: '))
                subnet = subnet_prediction(host)
                print(f'recommanded subnet: {subnet}')
                print(f'host available: {subnet.getResult_host()}')

            elif option == 3:
                IP_address = input('enter your IP address: ')
                prefix = int(input('enter your prefix: '))                    
                vlsm = VLSM_calculation(IP_address, prefix)

			
		
        except ValueError:
            print('please enter a correct value')

            

main()

