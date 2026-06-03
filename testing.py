import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from collections import deque

class Agent:
    def __init__(self, agent_id, wealth, consumption_rate):
        self.id = agent_id
        self.wealth = wealth
        self.consumption_rate = consumption_rate
        self.income_history = deque(maxlen=50)
        
class Producer:
    def __init__(self, producer_id, capital, productivity):
        self.id = producer_id
        self.capital = capital
        self.productivity = productivity
        self.revenue_history = deque(maxlen=50)

class Economy:
    def __init__(self, n_agents=50, n_producers=10):
        self.agents = [Agent(i, random.uniform(100, 500), random.uniform(0.6, 0.9)) 
                       for i in range(n_agents)]
        self.producers = [Producer(i, random.uniform(1000, 3000), random.uniform(0.5, 1.5)) 
                          for i in range(n_producers)]
        
        self.price = 10.0
        self.total_wealth_history = []
        self.price_history = []
        self.gini_history = []
        self.time = 0
        
    def calculate_gini(self):
        """Calculate Gini coefficient for wealth inequality"""
        wealths = sorted([a.wealth for a in self.agents])
        n = len(wealths)
        cum_wealth = sum((i + 1) * w for i, w in enumerate(wealths))
        return (2 * cum_wealth) / (n * sum(wealths)) - (n + 1) / n
    
    def step(self):
        """Run one simulation step"""
        self.time += 1
        
        # Calculate supply and demand
        total_demand = sum(a.wealth * a.consumption_rate / self.price for a in self.agents)
        total_supply = sum(p.capital * p.productivity for p in self.producers)
        
        # Adjust price based on supply/demand
        if total_demand > total_supply * 1.1:
            self.price *= 1.02
        elif total_demand < total_supply * 0.9:
            self.price *= 0.98
        
        self.price = max(1.0, min(50.0, self.price))
        
        # Agents consume and pay producers
        total_spending = 0
        for agent in self.agents:
            spending = min(agent.wealth * agent.consumption_rate, agent.wealth)
            agent.wealth -= spending
            total_spending += spending
            agent.income_history.append(agent.wealth)
        
        # Distribute revenue to producers
        for producer in self.producers:
            market_share = (producer.capital * producer.productivity) / max(total_supply, 1)
            revenue = total_spending * market_share
            producer.capital += revenue * 0.1  # 10% reinvestment
            producer.revenue_history.append(revenue)
            
        # Producers pay wages to agents (distribute wealth back)
        total_wages = total_spending * 0.7  # 70% goes to wages
        wage_per_agent = total_wages / len(self.agents)
        for agent in self.agents:
            agent.wealth += wage_per_agent
            # Small random income variation
            agent.wealth += random.uniform(-5, 5)
            agent.wealth = max(10, agent.wealth)  # Minimum wealth
        
        # Track metrics
        total_wealth = sum(a.wealth for a in self.agents)
        self.total_wealth_history.append(total_wealth)
        self.price_history.append(self.price)
        self.gini_history.append(self.calculate_gini())

class EconomyVisualizer:
    def __init__(self, economy):
        self.economy = economy
        self.fig, self.axes = plt.subplots(2, 2, figsize=(14, 10))
        self.fig.suptitle('Economic Simulation', fontsize=16)
        
    def animate(self, frame):
        """Animation function"""
        # Run simulation steps
        for _ in range(5):
            self.economy.step()
        
        # Clear all subplots
        for ax in self.axes.flat:
            ax.clear()
        
        # Plot 1: Wealth Distribution
        ax1 = self.axes[0, 0]
        wealths = [a.wealth for a in self.economy.agents]
        ax1.hist(wealths, bins=20, color='skyblue', edgecolor='black', alpha=0.7)
        ax1.set_title(f'Wealth Distribution (t={self.economy.time})')
        ax1.set_xlabel('Wealth')
        ax1.set_ylabel('Number of Agents')
        ax1.grid(True, alpha=0.3)
        
        # Plot 2: Price Over Time
        ax2 = self.axes[0, 1]
        ax2.plot(self.economy.price_history, color='green', linewidth=2)
        ax2.set_title('Market Price Over Time')
        ax2.set_xlabel('Time')
        ax2.set_ylabel('Price')
        ax2.grid(True, alpha=0.3)
        
        # Plot 3: Total Wealth Over Time
        ax3 = self.axes[1, 0]
        ax3.plot(self.economy.total_wealth_history, color='blue', linewidth=2)
        ax3.set_title('Total Economy Wealth')
        ax3.set_xlabel('Time')
        ax3.set_ylabel('Total Wealth')
        ax3.grid(True, alpha=0.3)
        
        # Plot 4: Gini Coefficient (Inequality)
        ax4 = self.axes[1, 1]
        ax4.plot(self.economy.gini_history, color='red', linewidth=2)
        ax4.set_title('Gini Coefficient (Inequality)')
        ax4.set_xlabel('Time')
        ax4.set_ylabel('Gini Coefficient')
        ax4.set_ylim(0, 1)
        ax4.axhline(y=0.4, color='orange', linestyle='--', label='High inequality threshold')
        ax4.legend()
        ax4.grid(True, alpha=0.3)
        
        plt.tight_layout()
    
    def run(self, frames=200, interval=100):
        """Run the animated visualization"""
        anim = animation.FuncAnimation(self.fig, self.animate, frames=frames, 
                                      interval=interval, repeat=False)
        plt.show()

# Run the simulation
if __name__ == "__main__":
    print("Starting Economic Simulation...")
    print("- 50 consumer agents with varying wealth")
    print("- 10 producers with different productivity levels")
    print("- Dynamic pricing based on supply and demand")
    print("- Tracking wealth distribution and inequality\n")
    
    economy = Economy(n_agents=50, n_producers=10)
    visualizer = EconomyVisualizer(economy)
    visualizer.run(frames=200, interval=100)
    
    print(f"\nSimulation completed!")
    print(f"Final average wealth: ${sum(a.wealth for a in economy.agents)/len(economy.agents):.2f}")
    print(f"Final price: ${economy.price:.2f}")
    print(f"Final Gini coefficient: {economy.gini_history[-1]:.3f}")