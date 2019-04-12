import urllib
from urllib import parse

def str2url(s):
    #s = '9hFaF2FF%_Et%m4F4%538t2i%795E%3pF.265E85.%fnF9742Em33e162_36pA.t6661983%x%6%%74%2i2%22735'
    num_loc = s.find('h')
    rows = int(s[0:num_loc])
    strlen = len(s) - num_loc
    cols = int(strlen/rows)
    right_rows = strlen % rows
    new_s = list(s[num_loc:])
    output = ''
    for i in range(len(new_s)):
        x = i % rows
        y = i / rows
        p = 0
        if x <= right_rows:
            p = x * (cols + 1) + y
        else:
            p = right_rows * (cols + 1) + (x - right_rows) * cols + y
        output += new_s[int(p)]
    return parse.unquote(output).replace('^', '0')


def main():
    s = "6hAFxn7255%5E25%58443ea2r65un8i3929f5fsniuu%44si5t%%%92DE5586.63daE519t%sie21EE2E3FE5586.F%m6e4Er%%d5e128b%_tplp38%_dEi235%618E48_mvD3f976ft21at4%%1F4818E48_mc3ie%%%a32%a%b%f%2c_%lsD72u%%d6DE5f881%13pkBae5e%8pF2m%%557271881%13pcD_x352tD63c535756ln3%_196s32%v18En16_5253ec95425%%8i22EE21%816_5253ox_pDE6i1pDdE6EcEuieD2t52ueD63i881%%91E71%yfd%54E32..FF%%4%5%%91E71%di%i8%do6s3251c63petn6s52pr%uDd16%35%58442%ae56e8"
    result_str = str2url(s)
    print(result_str)

if __name__ == '__main__':
    main()
