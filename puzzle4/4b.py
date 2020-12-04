import re

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

    valid = True

    print(passportFields)

    if 'byr' in passportFields:
        year = int(passportFields['byr'])
        if year < 1920 or year > 2002:
            valid = False
    else:
        valid = False

    if 'iyr' in passportFields:
        year = int(passportFields['iyr'])
        if year < 2010 or year > 2020:
            valid = False
    else:
        valid = False

    if 'eyr' in passportFields:
        year = int(passportFields['eyr'])
        if year < 2020 or year > 2030:
            valid = False
    else:
        valid = False

    if 'hgt' in passportFields:
        if not 'cm' in passportFields['hgt'] and not 'in' in passportFields['hgt']:
            valid = False
        else:
            number = int(passportFields['hgt'][:-2])
            unit = passportFields['hgt'][len(passportFields['hgt'])-2:]
            if unit == 'cm':
                if number < 150 or number > 193:
                    valid = False
            if unit == 'in':
                if number < 59 or number > 76:
                    valid = False
    else:
        valid = False

    if 'hcl' in passportFields:
        pattern = re.compile("#[0-9a-f]{6}")
        if pattern.search(passportFields['hcl']) is None:
            valid = False
    else:
        valid = False

    if 'ecl' in passportFields:
        if not passportFields['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
            valid = False
    else:
        valid = False

    if 'pid' in passportFields:
        if len(passportFields['pid']) > 9:
            valid = False
        else:
            pattern = re.compile("[0-9]{9}")
            if pattern.search(passportFields['pid']) is None:
                valid = False
    else:
        valid = False

    if valid:
        validCount += 1

print("Total number of passports: " + str(totalCount))
print("Number of valid passports: " + str(validCount))
print("Number of invalid passports: " + str(totalCount - validCount))
