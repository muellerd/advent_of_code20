passports = []

with open("C:\\Privat\\advent_of_code20\\puzzle4\\input1.txt") as f:
    empty = False
    passport = ""
    for line in f:
        if line.strip() == "":
            empty = True
        else:
            empty = False

        if empty:
            passports.append(passport.replace('\n', ' ').strip())
            passport = ""
        else:
            passport += line

print(passports)
validCount = 0
totalCount = 0

for passport in passports:
    passportFields = {}
    #print(passport)
    passportSplit = passport.split(' ')
    #print(passportSplit)
    for split in passportSplit:
        splitSplit = split.split(':')
        passportFields[splitSplit[0]] = splitSplit[1]

    print(passportFields)

    totalCount += 1

    if 'byr' in passportFields and 'iyr' in passportFields and 'eyr' in passportFields and 'hgt' in passportFields and 'hcl' in passportFields and 'ecl' in passportFields and 'pid' in passportFields:
        validCount += 1

print("Total number of passports: " + str(totalCount))
print("Number of valid passports: " + str(validCount))
print("Number of invalid passports: " + str(totalCount - validCount))
