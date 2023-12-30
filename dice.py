def calculate_total_combinations(number_of_faces, number_of_dice):
    total_combinations = number_of_faces ** number_of_dice
    return total_combinations

def main():
    number_of_faces = 6
    number_of_dice = 2

    # Calculate total combinations
    total_combinations = calculate_total_combinations(number_of_faces, number_of_dice)

    print("Total Combinations:", total_combinations)

if __name__ == "__main__":
    main()

print("****************************************************************************************************************************************************************")
def calculate_combination_distribution(sides):
    distribution_list = []

    for i in range(1, sides + 1):
        for j in range(1, sides + 1):
            total = i + j
            combination_map = {
                "Die A": i,
                "Die B": j,
                "Sum": total
            }
            distribution_list.append(combination_map)

    return distribution_list

def main():
    sides = 6

    # Calculate and display combination distribution
    combination_distribution = calculate_combination_distribution(sides)

    print("Distribution:")
    for combination_map in combination_distribution:
        print(combination_map)

if __name__ == "__main__":
    main()
print("******************************************************************************************************************************************************************")    
    
def calculate_sum_probability(sides):
    distribution = [0] * 11  # Index 0 corresponds to sum 2, index 10 corresponds to sum 12

    for i in range(1, sides + 1):
        for j in range(1, sides + 1):
            total = i + j
            distribution[total - 2] += 1

    probability_map = {}

    for i in range(2, 13):
        probability_map[i] = f"{distribution[i - 2]}/{36}"

    return probability_map

def main():
    sides = 6

    # Calculate and display sum probabilities
    sum_probability = calculate_sum_probability(sides)

    print("Probability of Sums:")
    for sum_value, prob in sum_probability.items():
        print(f"P(Sum = {sum_value}): {prob}")

if __name__ == "__main__":
    main()
