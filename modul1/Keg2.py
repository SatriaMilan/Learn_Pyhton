random_list = [105, 3.1, "hello", 737, "python", 2.7, "world", 412, 5.5, "AI"]


int_values = {}
float_values = ()
string_values = []


for item in random_list:
    if isinstance(item, int):
        satuan = item % 10
        puluhan = (item // 10) % 10
        ratusan = (item // 100) % 10
        
        int_values[item] = (ratusan, puluhan, satuan)
    elif isinstance(item, float):
       
        float_values += (item,)
    elif isinstance(item, str):
        
        string_values.append(item)

print("Nilai Integer (dalam bentuk dictionary):")
print(int_values)
print("\nNilai Float (dalam bentuk tuple):")
print(float_values)
print("\nNilai String (dalam bentuk list):")
print(string_values)