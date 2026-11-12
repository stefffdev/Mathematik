import re, sys
def fr(n, d): return f'<span class="fr"><span class="n">{n}</span><span class="d">{d}</span></span>'
def conv(s):
    s = re.sub(r'\{(\d+) (\d+)/(\d+)\}', lambda m: f'<span class="mx">{m[1]}{fr(m[2], m[3])}</span>', s)
    s = re.sub(r'\{([\d·]+)/([\d·]+)\}', lambda m: fr(m[1], m[2]), s)
    return s
src, dst = sys.argv[1], sys.argv[2]
open(dst, 'w').write(conv(open(src).read()))
