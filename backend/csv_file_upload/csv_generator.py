import csv


if __name__ == "__main__":
    print("run ...")
    try :            
        with open('./test.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["id", "email"])
            for i in range(100):
                writer.writerow([f"email{i+1}@gmail.com", f"002{i+1}_2"])
        
    except Exception as e:
        print(e)