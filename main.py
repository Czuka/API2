import pandas
import creopyson
import subprocess
import time

pathToCreoRunBat = "C://Program Files/PTC/Creo 7.0.1.0/Parametric/bin/parametric.bat"
pathToCreoMaterials = "C://Program Files/PTC/Creo 7.0.1.0/Common Files//text/materials-library/Standard-Materials_Granta-Design/Ferrous_metals//"
workingDirectory = "C:\Work\Api\kopia2"
modelFile = "projekcik.prt"

c = creopyson.Client()
print("check")
c.connect()
c.creo_set_creo_version(7)

print("check open is creo")
# Check creo is running
def open_creo():
    if c.is_creo_running():
        print("Creo running")
    else:
        subprocess.Popen(pathToCreoRunBat)
        time.sleep(50)
        open_creo()
open_creo()

model_inp = int(input("1: to open model\n"))
if model_inp == 1:
    c.creo_cd(workingDirectory)
    c.file_open(modelFile)
elif model_inp == 2:
    print("tak")


def print_table(tabela):
    print("Nw|A  |B  |C  |D  |E  |F ")
    for row in tabela:
        print(*row)


def select_parameters(parameter):
    parameters = {
        "W1": {"A": 100, "B": 100, "C": 8, "D": 100, "E": 36, "E2": 36, "F": 10, "F2": 10, "H": 2, "I": 0},
        "W2": {"A": 100, "B": 140, "C": 8, "D": 100, "E": 36, "E2": 36, "F": 10, "F2": 10, "H": 2, "I": 3},
        "W3": {"A": 100, "B": 180, "C": 8, "D": 100, "E": 36, "E2": 36, "F": 10, "F2": 10, "H": 2, "I": 4},
        "W4": {"A": 140, "B": 100, "C": 10, "D": 100, "E": 38, "E2": 38, "F": 12, "F2": 12, "H": 3, "I": 2},
        "W5": {"A": 140, "B": 140, "C": 10, "D": 100, "E": 38, "E2": 38, "F": 12, "F2": 12, "H": 3, "I": 3},
        "W6": {"A": 140, "B": 180, "C": 10, "D": 100, "E": 38, "E2": 38, "F": 12, "F2": 12, "H": 3, "I": 4},
        "W7": {"A": 180, "B": 100, "C": 11, "D": 100, "E": 40, "E2": 40, "F": 14, "F2": 14, "H": 4, "I": 2},
        "W8": {"A": 180, "B": 140, "C": 11, "D": 100, "E": 40, "E2": 40, "F": 14, "F2": 14, "H": 4, "I": 3},
        "W9": {"A": 180, "B": 180, "C": 11, "D": 100, "E": 40, "E2": 40, "F": 14, "F2": 14, "H": 4, "I": 4}
    }
    if parameter in parameters:
        return parameters[parameter]
    else:
        return None


def changeWorkingDirectory(newWorkingDirectory):
    workingDirectory = newWorkingDirectory
    c.creo_cd(workingDirectory)
    print("Your working directory: " + workingDirectory)



exit = True

while exit:
    print("0. Change working directory" +
          "\n1. Change model" +
          "\n2. Print raport" +
          "\n3. Change material" +
          "\n4. Export files" +
          "\n5. Save model" +
          "\n6. Exit")
    userInput = int(input("Enter your choice: "))
    match userInput:
        case 0:
            changeWorkingDirectory(input("Enter new working directory: "))
        case 1:
            tabela = [["W1", 100, 100, 8, 100, 36, 10],
                      ["W2", 100, 140, 8, 100, 36, 10],
                      ["W3", 100, 180, 8, 100, 36, 10],
                      ["W4", 140, 100, 10, 100, 38, 12],
                      ["W5", 140, 140, 10, 100, 38, 12],
                      ["W6", 140, 180, 10, 100, 38, 12],
                      ["W7", 180, 100, 11, 100, 40, 14],
                      ["W8", 180, 140, 11, 100, 40, 14],
                      ["W9", 180, 180, 11, 100, 40, 14]]
            print_table(tabela)
            while True:
                parameter = input("Prosze wpisac nazwe 'W' aby dobrac parametry: ")
                parameters = select_parameters(parameter)
                if parameters is not None:
                    break
                else:
                    print("Bledna nazwa")
                    print("Wpisz ponownie: ")
            A = parameters["A"]
            B = parameters["B"]
            C = parameters["C"]
            D = parameters["D"]
            E = parameters["E"]
            E2 = parameters["E2"]
            F = parameters["F"]
            F2 = parameters["F2"]
            H = parameters["H"]
            I = parameters["I"]

            c.dimension_set("A", value=A)
            c.dimension_set("B", value=B)
            c.dimension_set("C", value=C)
            c.dimension_set("E", value=E)
            c.dimension_set("E2", value=E2)
            c.dimension_set("F", value=F)
            c.dimension_set("F2", value=F2)
            c.dimension_set("H", value=H)
            if parameter !='W1':
                c.dimension_set("I", value=I)
            c.file_regenerate()
            c.feature_resume(name="M")
            c.feature_resume(name="N")
            if parameter == "W1":
                c.feature_suppress(name="M")
                c.feature_suppress(name="N")
            elif parameter == "W2" or parameter == "W3":
                c.feature_suppress(name="M")
            elif parameter == "W4" or parameter == "W7":
                c.feature_suppress(name="N")
            else:
                c.feature_resume(name="M") or c.feature_resume(name="N")
        case 2:
            masa = f"{c.file_massprops()['mass']:.3f}"
            with open(workingDirectory + '\\raport.txt', 'w') as f:
                f.write('\nNazwa:' + parameter)
                f.write('\nA=' + str(A))
                f.write('\nB=' + str(B))
                f.write('\nC=' + str(C))
                f.write('\nD=' + str(D))
                f.write('\nE=' + str(E))
                f.write('\nF=' + str(F))
                if parameter != 'W1':
                    f.write('\nI=' + str(I))
                f.write("\nNazwa materiału: " + c.file_get_cur_material())
                f.write("\nMasa modelu:" + masa)
        case 3:
            materials = ["Cast_iron_ductile.mtl", "Cast_iron_gray.mtl", "Cast_iron_malleable.mtl",
                         "Cast_iron_nodular.mtl", "Stainless_steel_austenitic.mtl", "Stainless_steel_ferritic.mtl",
                         "Stainless_steel_martensitic.mtl", "Steel_cast.mtl", "Steel_galvanized.mtl",
                         "Steel_high_carbon.mtl"]
            materialNumber = 0
            for x in materials:
                print(str(materialNumber) + ". " + x)
                materialNumber += 1
            materialNumberUserInput = int(input("Enter material number: "))
            c.file_load_material_file(materials[materialNumberUserInput], pathToCreoMaterials)
            c.file_set_cur_material(materials[materialNumberUserInput])
            c.file_regenerate()
            print("Material changed")
        case 4:
            c.interface_export_file("STEP")
            c.interface_export_3dpdf()
        case 5:
            c.file_save()
        case 6:
            exit = False
        case default:
            print("Wrong number, try again")

print("Changes has been showed after regenerating the model 'CTRL + G'")
input("")

