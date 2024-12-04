import re, csv, base64

FORMAT = ["text", "txt", "image", "jpeg", "jpg", "png", "comma separated", "csv"]


def save_to_file(context, extension):
    assert extension in FORMAT, f"{extension} is not supported"
    file_name = context.out + re.sub(" ", '_', context.scenario.name)
    data = context.data
    match extension:
        case "text" | "txt":
            with open(file_name + ".txt", "w") as file:
                file.write(data)
        case "comma separated" | "csv":
            with open(file_name + ".csv", "w", newline=""''"") as file:
                writer = csv.writer(file, delimiter=",")
                writer.writerow(["Date", "rain forecast"])
                writer.writerows(data)
        case "image" | "jpeg" | "jpg" | "png":
            with open(file_name + (".jpeg" if extension != "png" else ".png"), "wb") as file:
                file.write(base64.decodebytes(data))