import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.colors import ListedColormap

class IsingModel:
    def __init__(self, size=50, temperature=2.0, J=1.0):
        """
        Initialize the Ising model
        
        Parameters:
        size: Grid size (size x size)
        temperature: Temperature parameter (T)
        J: Coupling constant
        """
        self.size = size
        self.T = temperature
        self.J = J
        self.beta = 1.0 / temperature if temperature > 0 else float('inf')
        
        # Initialize random spin configuration (-1 or +1)
        self.spins = np.random.choice([-1, 1], size=(size, size))
        
        # Store history for plotting
        self.history = []
        self.magnetization_history = []
        self.energy_history = []
    
    def get_energy(self, i, j):
        """Calculate energy of a single spin at position (i,j)"""
        # Periodic boundary conditions
        neighbors = [
            self.spins[(i-1) % self.size, j],
            self.spins[(i+1) % self.size, j],
            self.spins[i, (j-1) % self.size],
            self.spins[i, (j+1) % self.size]
        ]
        return -self.J * self.spins[i, j] * sum(neighbors)
    
    def total_energy(self):
        """Calculate total energy of the system"""
        energy = 0
        for i in range(self.size):
            for j in range(self.size):
                energy += self.get_energy(i, j)
        return energy / 2  # Divide by 2 to avoid double counting
    
    def magnetization(self):
        """Calculate total magnetization"""
        return np.sum(self.spins)
    
    def monte_carlo_step(self):
        """Perform one Monte Carlo step (Metropolis algorithm)"""
        for _ in range(self.size * self.size):
            # Choose random spin
            i, j = np.random.randint(0, self.size, 2)
            
            # Calculate energy change if we flip this spin
            current_energy = self.get_energy(i, j)
            # Flip the spin temporarily
            self.spins[i, j] *= -1
            new_energy = self.get_energy(i, j)
            
            delta_E = new_energy - current_energy
            
            # Accept or reject the flip
            if delta_E <= 0 or np.random.random() < np.exp(-self.beta * delta_E):
                # Accept the flip (spin is already flipped)
                pass
            else:
                # Reject the flip (flip back)
                self.spins[i, j] *= -1
    
    def run_simulation(self, steps):
        """Run the simulation for given number of steps"""
        for step in range(steps):
            self.monte_carlo_step()
            
            # Store snapshots for animation
            if step % 10 == 0:  # Store every 10th step
                self.history.append(self.spins.copy())
                self.magnetization_history.append(self.magnetization())
                self.energy_history.append(self.total_energy())

def create_ising_animation(size=50, temperature=2.0, steps=1000):
    """Create an animated visualization of the Ising model"""
    
    # Create the model
    model = IsingModel(size=size, temperature=temperature)
    
    # Run simulation
    print(f"Running Ising model simulation...")
    print(f"Grid size: {size}x{size}")
    print(f"Temperature: {temperature}")
    print(f"Steps: {steps}")
    
    model.run_simulation(steps)
    
    # Set up the figure and subplots
    fig = plt.figure(figsize=(15, 5))
    
    # Spin configuration plot
    ax1 = plt.subplot(131)
    ax1.set_title('Spin Configuration')
    ax1.set_xlabel('x')
    ax1.set_ylabel('y')
    
    # Custom colormap: blue for -1, red for +1
    colors = ['blue', 'red']
    cmap = ListedColormap(colors)
    
    im = ax1.imshow(model.history[0], cmap=cmap, vmin=-1, vmax=1, animated=True)
    plt.colorbar(im, ax=ax1, ticks=[-1, 1], label='Spin')
    
    # Magnetization plot
    ax2 = plt.subplot(132)
    ax2.set_title('Magnetization vs Time')
    ax2.set_xlabel('Time Step (×10)')
    ax2.set_ylabel('Total Magnetization')
    line1, = ax2.plot([], [], 'g-', linewidth=2)
    ax2.grid(True, alpha=0.3)
    
    # Energy plot
    ax3 = plt.subplot(133)
    ax3.set_title('Energy vs Time')
    ax3.set_xlabel('Time Step (×10)')
    ax3.set_ylabel('Total Energy')
    line2, = ax3.plot([], [], 'r-', linewidth=2)
    ax3.grid(True, alpha=0.3)
    
    # Set axis limits for time series plots
    time_steps = range(len(model.magnetization_history))
    if time_steps:
        ax2.set_xlim(0, max(time_steps))
        ax2.set_ylim(min(model.magnetization_history) * 1.1, 
                     max(model.magnetization_history) * 1.1)
        
        ax3.set_xlim(0, max(time_steps))
        ax3.set_ylim(min(model.energy_history) * 1.1, 
                     max(model.energy_history) * 1.1)
    
    plt.tight_layout()
    
    def animate(frame):
        """Animation function"""
        if frame < len(model.history):
            # Update spin configuration
            im.set_array(model.history[frame])
            
            # Update magnetization plot
            x_data = list(range(frame + 1))
            y_data = model.magnetization_history[:frame + 1]
            line1.set_data(x_data, y_data)
            
            # Update energy plot
            y_data2 = model.energy_history[:frame + 1]
            line2.set_data(x_data, y_data2)
            
            # Update title with current step
            ax1.set_title(f'Spin Configuration (Step {frame * 10})')
        
        return [im, line1, line2]
    
    # Create animation
    anim = animation.FuncAnimation(fig, animate, frames=len(model.history),
                                   interval=100, blit=True, repeat=True)
    
    plt.show()
    
    return model, anim

def compare_temperatures():
    """Compare Ising model behavior at different temperatures"""
    temperatures = [0.5, 1.5, 2.27, 3.0, 5.0]  # 2.27 is near critical temperature
    fig, axes = plt.subplots(2, len(temperatures), figsize=(20, 8))
    
    colors = ['blue', 'red']
    cmap = ListedColormap(colors)
    
    for i, T in enumerate(temperatures):
        model = IsingModel(size=30, temperature=T)
        model.run_simulation(500)
        
        # Final configuration
        axes[0, i].imshow(model.spins, cmap=cmap, vmin=-1, vmax=1)
        axes[0, i].set_title(f'T = {T}')
        axes[0, i].set_xticks([])
        axes[0, i].set_yticks([])
        
        # Magnetization evolution
        axes[1, i].plot(model.magnetization_history, 'g-', linewidth=2)
        axes[1, i].set_xlabel('Time Step (×10)')
        axes[1, i].set_ylabel('Magnetization')
        axes[1, i].grid(True, alpha=0.3)
        axes[1, i].set_title(f'M(t), T = {T}')
    
    axes[0, 0].set_ylabel('Final Configuration')
    axes[1, 0].set_ylabel('Magnetization')
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # Example 1: Animated simulation at moderate temperature
    print("Creating Ising model animation...")
    model, anim = create_ising_animation(size=40, temperature=0.5, steps=1000)
    
    # Example 2: Compare different temperatures
    print("\nComparing different temperatures...")
    compare_temperatures()
    
    # Example 3: Quick analysis of final state
    print(f"\nFinal Statistics:")
    print(f"Final magnetization: {model.magnetization()}")
    print(f"Final energy: {model.total_energy()}")
    print(f"Average magnetization: {np.mean(model.magnetization_history):.2f}")
    print(f"Magnetization std: {np.std(model.magnetization_history):.2f}")