# Part 1 = 43699799094202
def clear():
    a = dir()
    for v in a:
        exec(f'del {v}', globals())

def process_operation():
    return 0


def do_op(values, one, two, op):
    if op == '+':
        try:
            return values[one] + values[two], True
        except KeyError:
            return 0, False
    if op == '-':
        try:
            return values[one] - values[two], True
        except KeyError:
            return 0, False
    if op == '*':
        try:
            return values[one] * values[two], True
        except KeyError:
            return 0, False
    if op == '/':
        try:
            return values[one] / values[two], True
        except KeyError:
            return 0, False
    print(f"What operation is {op}")
    return 0, False

import copy
import aocd
raw = aocd.get_data(day=21, year=2022)
data1 = raw.splitlines()

values = {}
for d in data1:
    if len(d.split(' ')) == 2:
        if not ((d[0] == 'h') and (d[1] == 'u') and (d[2] == 'm') and (d[3] == 'n')):
            values[d[0:4]] = int(d[6:])
            #print(f"Adding {d} as {d[0:4]}  {int(d[6:])}")

#print(len(values))
values["humn"] = 3375719472770

# Process first pass to see what depends just on hardcoded values
cnt = 1
while cnt > 0:
    cnt = 0
    for d in data1:
        if len(d.split(' ')) != 2:
            dest = d[0:4]
            one = d[6:10]
            two = d[13:17]
            op = d[11]
            if dest not in values.keys():
                value,succ = do_op(values, one, two, op)
                if succ:
                    values[dest] = value
                    cnt += 1

#print(len(values))

leftovers = []
for d in data1:
    if len(d.split(' ')) != 2:
        dest = d[0:4]
        one = d[6:10]
        two = d[13:17]
        op = d[11]
        if dest not in values.keys():
            leftovers.append([dest, one, two, op])

import pdb;pdb.set_trace()
# Stuff below didn't work... maybe sbtm is not an integer?
# Maybe build sbtm symbolically
#['sbfn', 'lwgr', 'rrfg', '-'], ['hpnl', 'vslw', 'nnzq', '*'], ['vbdq', 'bfcg', 'lnhs', '+'], ['stzw', 'hstf', 'wlmv', '/'], ['jbmw', 'wdmp', 'rtzg', '/'], ['vcbj', 'jbmw', 'wbfn', '+'], ['wdmp', 'mmqh', 'lgfd', '+'], ['lwjd', 'vmfc', 'bdvv', '/'], ['fgrn', 'bsbv', 'zmrb', '-'], ['mlvd', 'pbts', 'fgrn', '*'], ['wtzd', 'mlvd', 'lpph', '+'], ['mhgp', 'rrpc', 'vwfz', '/'], ['sbtm', 'glgl', 'lzth', '*'], ['vmcp', 'fpzj', 'tjgf', '-'], ['cfsw', 'vcbj', 'qztd', '+'], ['fpzj', 'cfsw', 'mzqs', '/'], ['mvth', 'jpzs', 'zdwl', '*'], ['drdn', 'ppwg', 'rlwp', '+'], ['rrpc', 'brnr', 'mzrn', '+'], ['nhvm', 'vbbc', 'mfgn', '-'], ['bsbv', 'drdn', 'ztbw', '/'], ['ntnz', 'wtzd', 'tsqs', '*'], ['lgfd', 'hsdt', 'pgfh', '*'], ['bmln', 'sbfn', 'pjlm', '*'], ['gmqj', 'dvmr', 'lqhs', '+'], ['zlmt', 'fhhm', 'tbdr', '-'], ['zdwl', 'humn', 'bnrn', '-'], ['hvbc', 'mbms', 'mvth', '+'], ['bjzn', 'nfnd', 'mrsv', '-'], ['dzbb', 'tvss', 'pjbq', '+'], ['dnnd', 'rbgn', 'btvh', '+'], ['ssvt', 'lqrf', 'hmpc', '+'], ['phrf', 'lghg', 'sbrw', '+'], ['whwg', 'hpnl', 'ttnn', '+'], ['fhhm', 'whwg', 'mnzw', '*'], ['pgfh', 'lggr', 'bjmv', '-'], ['glsj', 'mrmh', 'ghmj', '+'], ['sbrw', 'bgtd', 'gfmb', '*'], ['glgl', 'zsvb', 'frlr', '-'], ['rlwp', 'gzdf', 'rfvr', '*'], ['tztg', 'ttgc', 'lsnd', '+'], ['mzsz', 'stzw', 'zshf', '-'], ['frpz', 'ntnz', 'cbnz', '-'], ['lggr', 'phrf', 'nlzl', '/'], ['bfcg', 'pvpf', 'nhvm', '*'], ['vslw', 'gnzh', 'lwjd', '+'], ['lwgr', 'dnnd', 'vlqw', '/'], ['fgvl', 'zlmt', 'ldwz', '/'], ['dvmr', 'ssvt', 'pptf', '/'], ['vbbc', 'mzsz', 'nsbn', '*'], ['hstf', 'lphl', 'fgvl', '+'], ['pjbq', 'frpz', 'tcfr', '/'], ['zsfh', 'ddrv', 'lwgv', '-'], ['vmfc', 'lmft', 'gfqg', '-'], ['lqrf', 'mhgp', 'lsrs', '-'], ['mrmh', 'vmcp', 'vwml', '*'], ['lmft', 'gmqj', 'dhlr', '*'], ['gzdf', 'bbgj', 'vbgb', '-'], ['pvww', 'hvbc', 'fmhl', '/'], ['bbgj', 'tztg', 'tgtm', '/'], ['ttgc', 'vbdq', 'zfjh', '/'], ['rbgn', 'pvww', 'qdfw', '+'], ['bgtd', 'bmln', 'vnhl', '-'], ['mzrn', 'prcg', 'zsfh', '*'], ['frlr', 'dzbb', 'bqqw', '/'], ['nfnd', 'glsj', 'jwsn', '*'], ['root', 'sbtm', 'bmgf', '+'], ['ddrv', 'bjzn', 'cjbw', '/']]
sbtm = (glgl * lzth)
sbtm = ((zsvb - frlr) * lzth)
sbtm = ((zsvb - (dzbb / bqqw) * lzth)
 ...

#print(leftovers)
#print(values["sbtm"]) (not yet defined)
#print(values["bmgf"]) # 12725480108701
#values["humn"] = 0
#diff = []
#for h in range(0,1):
#    v2 = copy.deepcopy(values)
#    #print(f"Try {h}")
#    values.update({"humn":h})
#    while "sbtm" not in v2.keys():
#        for l in leftovers:
#            dest = l[0]
#            one = l[1]
#            two = l[2]
#            op = l[3]
#            if dest not in v2.keys():
#                value,succ = do_op(v2, one, two, op)
#                if succ:
#                    v2[dest] = value
#    #print(f"{h}: {v2['sbtm']-v2['bmgf']}")
#    diff.append(v2['sbtm']-v2['bmgf'])
#
#print(f"Min diff = {min(diff)}")
#print(f"Min at = {diff.index(min(diff))}")


# STOLEN
#from functools import reduce
#
#parse = lambda line: {line[:4]: line[6:-1].split(" ")}
#ast_nodes = reduce(lambda a, b: a | b, (parse(x) for x in open('data.txt')))
#print(ast_nodes)
#def sub(name):
#    expr = ast_nodes[name]
#    if (name == "humn"): return "humn"
#    if (len(expr) == 1): return expr[0]
#    left, op, right = expr
#    if (name == "root"): op = "-"
#    return f"({sub(left)}){op}({sub(right)})"
#
#fn = eval(f"lambda humn: {sub('root')}")
#fn2 = eval(f"lambda humn: {sub('bmgf')}")
#fn3 = eval(f"lambda humn: {sub('sbtm')}")
#a, b = [x*100000000000000 for x in [-1, 1]]
#while(True):
#    c = (b + a) // 2;
#    #print(c)
#    print(fn2(c))
#    print(fn3(c))
#    #print(sub('root'))
#    if (fn(c) == 0): print(c); break
#    if (fn(c) * fn(a) < 0): b = c
#    else: a = c;
