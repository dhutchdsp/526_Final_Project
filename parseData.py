import sys

def parse_files(input_file_name, output_file_name):
    # Open both files in binary mode
    with open(input_file_name, mode="r") as input_file, open(output_file_name, mode="w") as output_file:
        title = input_file.readline()
        line2 = input_file.readline()
        allLines = input_file.readlines()
        
        uniqueGPSpoints = []

        #Remove packet data
        for l in allLines:
            if l[0] == "r":
                pass
            elif l[0] == "<":
                gpsString = l[2:27]
                if gpsString not in uniqueGPSpoints:
                    uniqueGPSpoints.append(gpsString)
        
        for point in uniqueGPSpoints:
            output_file.write(point + ",black,square\n")




if __name__ == "__main__":
    # Create simpler argument array

    fileDirectorIN = "TestDataIn/"
    fileDirectoryOUT = "TestDataOut/"

    infiles = ["note0.txt", "note1.txt", "note2.txt", "note3.txt", "note4.txt", "note5.txt", "note6.txt"]
    outfiles = ["note0out.txt", "note1out.txt", "note2out.txt", "note3out.txt", "note4out.txt", "note5out.txt", "note6out.txt"]

    for i in range(len(infiles)):
        parse_files(fileDirectorIN + infiles[i], fileDirectoryOUT + outfiles[i])
