from collections import deque

class AuctionSystem:
    def __init__(self):
        self.auction_items = []  # List for all auction items
        self.bidder_queue = deque()  # Queue for bidders
        self.recent_bids = []  # Stack for recently bid items
    
    # Add item to auction
    def add_item(self, item):
        self.auction_items.append(item)
        print(f"Item added to auction: {item}")
    
    # Add bidder to queue
    def add_bidder(self, bidder):
        self.bidder_queue.append(bidder)
        print(f"Bidder {bidder} added to queue")
    
    # Bid on an item
    def bid_on_item(self, bidder, item):
        if item not in self.auction_items:
            print(f"Item {item} is not in the auction")
            return
        
        self.recent_bids.append((bidder, item))  # Stack for recent bids
        print(f"Bidder {bidder} bid on {item}")
    
    # Process next bidder from queue
    def process_next_bidder(self):
        if self.bidder_queue:
            next_bidder = self.bidder_queue.popleft()  # FIFO for bidder processing
            print(f"Processing next bidder: {next_bidder}")
        else:
            print("No bidders to process")
    
    # Show recently bid items (stack)
    def show_recent_bids(self):
        if self.recent_bids:
            print("Recently bid items:")
            for bid in reversed(self.recent_bids):  # Show stack top-to-bottom
                print(f"{bid[0]} bid on {bid[1]}")
        else:
            print("No recent bids")
    
# Example usage:
auction = AuctionSystem()

# Adding auction items
auction.add_item("Painting")
auction.add_item("Vase")
auction.add_item("Antique Clock")

# Adding bidders
auction.add_bidder("Alice")
auction.add_bidder("Bob")

# Bidding on items
auction.bid_on_item("Alice", "Painting")
auction.bid_on_item("Bob", "Vase")

# Show recent bids
auction.show_recent_bids()

# Processing next bidder in queue
auction.process_next_bidder()
auction.process_next_bidder()

# Attempting to process when no bidders left
auction.process_next_bidder()