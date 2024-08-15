def count_slov(lowered_string):
    character_count = {}
    
    for char in lowered_string:
        if char in character_count:
            character_count[char] += 1
        else:
            character_count[char] = 1
            
    # Фильтруем только повторяющиеся символы
    repeated_characters = {char: count for char, count in character_count.items() if count > 1}
    return repeated_characters

def sort_and_print(character_counts):
    # Сортируем по алфавиту
    sorted_items = sorted(character_counts.items())
    for char, count in sorted_items:
        print(f"The '{char}' character was found {count} times")

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print (f"{len(file_contents.split())} words found in the document")
        lowered_string = file_contents.lower()
        result = count_slov(lowered_string)
        sort_and_print(result)

main()
