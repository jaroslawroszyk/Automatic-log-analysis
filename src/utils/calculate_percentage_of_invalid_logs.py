def calculate_percentage_of_invalid_logs(incorrect_logs, number_of_logs):
    if incorrect_logs > 0:
        procent_wadliwych_logow = str(
            round((incorrect_logs / number_of_logs) * 100, 1))
    else:
        procent_wadliwych_logow = "0.0"
    return procent_wadliwych_logow
