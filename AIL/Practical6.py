positive_criteria = {
    "exceeds_deadlines": 5,
    "high_quality_work": 4,
    "great_team_player": 3,
    "consistently_improves": 2,
    "excellent_communication": 1,
}

negative_criteria = {
    "misses_deadlines": -5,
    "poor_quality_work": -4,
    "poor_team_player": -3,
    "resistant_to_feedback": -2,
    "poor_communication": -1,
}
#rule engine
def evaluate_employee(positives, negatives):
    score = 0
    for pos in positives:
        score += positive_criteria.get(pos, 0)
    
    for neg in negatives:
        score += negative_criteria.get(neg, 0)
    
    return score
#user interface

def user_interface():
    print("Employee Performance Evaluation")
    print("Please enter positive criteria from the list below, separated by commas:")
    for criterion in positive_criteria:
        print(f"- {criterion}")
    print("\n")
    positives_input = input("> ")
    print("\n")
    
    print("Please enter negative criteria from the list below, separated by commas:")
    for criterion in negative_criteria:
        print(f"- {criterion}")
    print("\n")
    negatives_input = input("> ")
    print("\n")
    
    positives = [item.strip() for item in positives_input.split(",") if item.strip() != ""]
    negatives = [item.strip() for item in negatives_input.split(",") if item.strip() != ""]
    
    print(positives, negatives)
    
    if not positives and not negatives:
        print("No criteria entered. Exiting.")
        return
    
    score = evaluate_employee(positives, negatives)
    print(f"Employee Score: {score}")
    print("\n")
    
    if score > 10:
        print("Performance: Outstanding")
    elif score > 5:
        print("Performance: Good")
    elif score > 0:
        print("Performance: Satisfactory")
    else:
        print("Performance: Needs Improvement")

if __name__ == "__main__":
    user_interface()