def merge_and_sort(list1, list2):
    # Об'єднання двох списків
    combined = list1 + list2

    # Алгоритм сортування бульбашкою
    n = len(combined)
    for i in range(n):
        for j in range(0, n - i - 1):
            if combined[j] > combined[j + 1]:
                # Обмін елементів
                combined[j], combined[j + 1] = combined[j + 1], combined[j]

    return combined

# Приклад використання
list_a = [5, 2, 9]
list_b = [1, 7, 3]
sorted_list = merge_and_sort(list_a, list_b)
print("Впорядкований список:", sorted_list)

