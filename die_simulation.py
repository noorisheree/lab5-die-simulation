import numpy as np
import matplotlib.pyplot as plt

# Set seed for reproducible results
np.random.seed(42)

# Roll a fair six-sided die 1000 times
rolls = np.random.randint(1, 7, size=1000)

# Print first 10 rolls
print("First 10 rolls:", rolls[:10])

# Count occurrences of each face
faces, counts = np.unique(rolls, return_counts=True)

# Theoretical probability
theoretical_probability = 1 / 6

# Print results
print("\nFace Count Empirical P Theoretical P")

for face, count in zip(faces, counts):
    empirical_probability = count / 1000
    print(
        f"{face} {count:5d} "
        f"{empirical_probability:.3f} "
        f"{theoretical_probability:.4f}"
    )

# Plot histogram
plt.figure(figsize=(8, 5))

plt.hist(
    rolls,
    bins=np.arange(0.5, 7.5, 1),
    edgecolor="black"
)

plt.xticks(range(1, 7))
plt.xlabel("Die Face")
plt.ylabel("Frequency")
plt.title("Fair Die Rolls - 1000 Simulations")

plt.tight_layout()

# Save the plot
plt.savefig("die_rolls.png")

print("\nSaved die_rolls.png")

# Display the plot
plt.show()