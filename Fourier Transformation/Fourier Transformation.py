import numpy as np                   # NumPy: অ্যারে এবং ম্যাথ অপারেশনের জন্য
import matplotlib.pyplot as plt      # Matplotlib: গ্রাফ অঙ্কনের জন্য

x = np.array([1, 5, 2, 6])           # সিগন্যাল x[n] তৈরি
N = len(x)                            # সিগন্যালের দৈর্ঘ্য
print(f"Length of x: {N}")            # দৈর্ঘ্য প্রিন্ট

X = np.fft.fft(x)                     # x[n] এর DFT (Discrete Fourier Transform) নেওয়া
n = np.arange(N)                      # n = 0 থেকে N-1 পর্যন্ত ইনডেক্স অ্যারে

# মূল সিগন্যাল ও DFT প্লট
plt.figure(figsize=(12,6))            # ফিগারের আকার নির্ধারণ
plt.subplot(2,2,1)                    # সাবপ্লট 2x2 এর মধ্যে 1ম
plt.stem(n, x, basefmt=" ")           # x[n] এর স্টেম প্লট
plt.title("Original signal x[n]")
plt.xlabel("n")
plt.ylabel("Amplitude")

plt.subplot(2,2,2)                    # সাবপ্লট 2x2 এর মধ্যে 2য়
plt.stem(np.arange(N), np.abs(X), basefmt=" ")  # DFT magnitude |X[k]|
plt.title("DFT Magnitude |X[k]|")
plt.xlabel("k")
plt.ylabel("Magnitude")

plt.subplot(2,2,4)                    # সাবপ্লট 2x2 এর মধ্যে 4র্থ
plt.stem(np.arange(N), np.angle(X), basefmt=" ") # DFT phase ∠X[k]
plt.title("DFT Phase ∠X[k]")
plt.xlabel("k")
plt.ylabel("Phase")

plt.tight_layout()                     # লেআউট ঠিক করা
plt.show()                             # সব প্লট দেখানো

# প্রতিটি ফ্রিকুয়েন্সি কম্পোনেন্টের টাইম-ডোমেইন অংশ আলাদা করে প্লট
t = np.arange(N)
plt.figure(figsize=(10,6))
for k in range(N):
    component = (1/N) * X[k] * np.exp(1j*2*np.pi*k*t/N)
    # k-তম ফ্রিকুয়েন্সি কম্পোনেন্ট (IDFT-এর অংশ)
    print(component.real)              # কম্পোনেন্টের বাস্তব অংশ প্রিন্ট

    plt.subplot(N, 1, k+1)             # Nটি সাবপ্লট, k-তম
    plt.stem(t, component.real, basefmt=" ") # বাস্তব অংশের স্টেম প্লট
    plt.title(f"Frequency Component k={k}, f={k/N}")
    plt.ylabel("Real part")

plt.xlabel("n")
plt.tight_layout()
plt.show()
