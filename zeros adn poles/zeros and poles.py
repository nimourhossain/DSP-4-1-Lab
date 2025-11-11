import sympy as sp                # SymPy: সিম্বলিক গণনা (প্রতীকী গাণিতিক) লাইব্রেরি
import numpy as np                # NumPy: নম্বর এবং অ্যারে অপারেশনের জন্য
import matplotlib.pyplot as plt   # Matplotlib: প্লট/চার্ট আঁকার জন্য

z = sp.symbols('z')               # 'z' কে SymPy-র একটি প্রতীক (symbol) হিসেবে ডিফাইন করা হলো
x = [1, 2, 5, 0, 6, 3]            # সময়-ডোমেইন সিগন্যাল x[n] (কম্পোনেন্ট তালিকা)

Xz = sum(x[n] * z**(-n) for n in range(len(x)))
# X(z): x[n] এর Z-রূপ, sum of x[n] z^{-n}

print("Z-transform X(z):", Xz.simplify())
# প্রতীকী রূপটি সহজ করে প্রিন্ট করা হলো

Xz_poly = sp.together(Xz * z**(len(x)-1)).as_numer_denom()[0]
# X(z) কে গুণ করে z^{N-1} করলে নুমেরেটরটি পলিনোম হবে; এটিকে বের করা হলো

print("Polynomial form:", Xz_poly)
# পলিনোমিয়াল নুমেরেটর প্রিন্ট

coeffs = sp.Poly(Xz_poly, z).all_coeffs()
# পলিনোমের সব কোএফিসিয়েন্ট (উচ্চতর ডিগ্রি থেকে নিম্নতর) পাওয়া হলো

coeffs = [complex(c) for c in coeffs]
# SymPy সংখ্যা গুলোকে Python complex টাইপ-এ কনভার্ট করা হলো (np.roots দরকার)

zeros = np.roots(coeffs)
# পলিনোমের রুটগুলো — এগুলো হলো Z-ট্রান্সফর্মের zeros

poles = [0]*(len(x)-1)
# x[n] এর causal sequence হলে poles থাকে z=0 তে (গণনা অনুসারে N-1 পোল)

plt.figure(figsize=(6,6))
plt.axhline(0, color='black')     # বাস্তব অক্ষ (x-অক্ষ) আঁকা
plt.axvline(0, color='black')     # কাল্পনিক অক্ষ (y-অক্ষ) আঁকা
plt.scatter(np.real(zeros), np.imag(zeros), marker='o', color='b', label='Zeros')
# zeros প্লট করা হলো নীল বৃত্তে
plt.scatter(np.real(poles), np.imag(poles), marker='x', color='r', label='Poles')
# poles প্লট করা হলো লাল ক্রসে
plt.xlabel("Real")
plt.ylabel("Imag")
plt.title("Pole-Zero Plot")
plt.legend()
plt.grid(True)
plt.show()
# পোল-জিরো প্লট দেখানো হলো
