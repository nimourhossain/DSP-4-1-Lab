import numpy as np                      # NumPy: অ্যারে ও গণিত অপারেশনের জন্য
import matplotlib.pyplot as plt         # গ্রাফ আঁকার জন্য matplotlib.pyplot

n = np.arange(-10, 11)                  # n = -10 থেকে 10 পর্যন্ত ইন্টেজার অ্যারে তৈরি
x = np.array([abs(i) if -3 <= i <= 3 else 0 for i in n])
# x: শুধুমাত্র n ∈ [-3,3] তাতে |n| মান আছে, অন্যথায় 0 (ট্রাঙ্কেটেড ভেরটেক্স শেপ)

# অপারেশনগুলো
y_a = x                                  # (a) y(n) = x(n) — অরিজিনাল সিগন্যাল
y_b = np.roll(x, 1)                      # (b) y(n) = x(n-1) — ডান দিকে এক স্টেপ শিফট
y_c = np.roll(x, -1)                     # (c) y(n) = x(n+1) — বাম দিকে এক স্টেপ শিফট
y_d = (np.roll(x,-1) + x + np.roll(x,1))/3
# (d) পাশের দুইটি এবং নিজেকে গড় করে নেওয়া (3-পয়েন্ট মুভিং অ্যাভারেজ)

y_e = np.maximum(np.maximum(np.roll(x,-1), x), np.roll(x,1))
# (e) প্রতিটি স্থানে তিনটি মানের মধ্যে সর্বোচ্চ নেওয়া (3-পয়েন্ট ম্যাক্স ফিল্টার)

y_f = np.cumsum(x)                       # (f) k<=n পর্যন্ত x(k)-এর ধাপে ধাপে যোগফল (কিউমুলেটিভ সাম)

results = [y_a, y_b, y_c, y_d, y_e, y_f]  # সব আউটপুট লিস্টে রাখা হলো
titles = ['(a) y(n) = x(n)',
          '(b) y(n) = x(n - 1)',
          '(c) y(n) = x(n + 1)',
          '(d) y(n) = (1/3)[x(n+1) + x(n) + x(n - 1)]',
          '(e) y(n) = max(x(n+1), x(n), x(n - 1))',
          '(f) y(n) = cumulative sum of x(k)']

fig, axs = plt.subplots(6, 1, figsize=(8,12), sharex=True)
# ছয়টি সাবপ্লট এক কলামে তৈরি; x-অক্ষ শেয়ার করা হয়েছে

for i in range(6):
    axs[i].stem(n, results[i], basefmt=" ")  # প্রতিটি সাবপ্লটে স্টেম প্লট আঁকা
    axs[i].set_ylabel("y(n)")                # y-অক্ষ লেবেল
    axs[i].set_title(titles[i])              # টাইটেল সেট করা
    axs[i].grid(True)                        # গ্রিড চালু

axs[-1].set_xlabel("n")                      # নিচের প্লটের x-অক্ষে 'n' লেবেল
plt.tight_layout()                           # লেআউট এডজাস্ট করে স্পেস ঠিক করা
plt.show()                                   # সব প্লট দেখানো
