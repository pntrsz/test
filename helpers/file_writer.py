import re, csv, base64

supported_formats = ["text", "txt", "image", "jpeg", "jpg", "png", "comma separated", "csv"]


@staticmethod
def save_to_file(extension, scenario_name, data):
    assert extension in supported_formats, f"{extension} is not supported"
    file_name = "./out/" + re.sub(" ", '_', scenario_name)
    match extension:
        case "text", "txt":
            with open(file_name + ".txt", "w") as file:
                file.write(data)
        case "comma separated", "csv":
            with open(file_name + ".csv", "w", newline=""''"") as file:
                writer = csv.writer(file, delimiter=",")
                writer.writerow(["Date", "rain forecast"])
                writer.writerows(data)
        case "image", "jpeg", "jpg", "png":
            with open(file_name + (".jpeg" if extension != "png" else ".png"), "wb") as file:
                file.write(base64.decodebytes(data))
