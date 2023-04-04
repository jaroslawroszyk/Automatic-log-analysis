def calculate_percentage_of_invalid_logs(incorrect_logs, number_of_logs):
    if incorrect_logs > 0:
        procent_wadliwych_logow = str(
            round((incorrect_logs / number_of_logs) * 100, 1))
    else:
        procent_wadliwych_logow = "0.0"
    return procent_wadliwych_logow

def calculate_error_logs_percentage(incorrect_logs, number_of_logs, correct_logs):
    if incorrect_logs > 0:
        error_logs_percentage = round((incorrect_logs / number_of_logs) * 100, 1)
        error_logs_percentage_str = str(error_logs_percentage)
    elif incorrect_logs == 0 and len(correct_logs) > 0:
        error_logs_percentage_str = "0.0"
    else:
        error_logs_percentage_str = "100.0"
    
    return error_logs_percentage_str
