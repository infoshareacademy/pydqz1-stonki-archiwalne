from generator_function import generate_male_name, generate_female_name, generate_address, generate_female_person, \
    write_Json_to_file, generate_unisex_last_name, generate_male_last_name, generate_nick

print(generate_male_name())
print(generate_female_name())
print(generate_unisex_last_name())
print(generate_address())
write_Json_to_file(generate_female_person)
generate_male_last_name()
print(generate_nick())
