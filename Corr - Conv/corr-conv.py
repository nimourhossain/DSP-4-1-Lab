import numpy as np                      # NumPy: অ্যারে ও গণিতের জন্য
from scipy.signal import correlate, convolve  # SciPy-এর সিগন্যাল টুল থেকে correlate ও convolve ফাংশন আনছি

x = np.array([1, 2, 3])                 # সিগন্যাল x (টাইম-ডোমেইন সিগন্যাল) তৈরি
h = np.array([0, 0.5, 1])               # ফিল্টার/ইনপুট h তৈরি (ইমপাল্স রেসপন্স)

conv = convolve(x, h, mode='full')      # x * h এর লিনিয়ার কনভোলিউশন (पूर्ण আউটপুট)
corr = correlate(x, h, mode='full')     # x এবং h-এর ক্রস-কোরিলেশন (পূর্ণ আউটপুট)

# আউটপুট প্রিন্ট: প্রতিটি উপাদানকে float-এ কনভার্ট করে দেখানো
print("Convolution:", [float(i) for i in conv])
print("Correlation:", [float(i) for i in corr])
