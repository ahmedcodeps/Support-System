from collections import deque
from datetime import datetime


requests = {}        # dictionary for requests  
request_ids = set()  # storing request ids

request_queue = deque()  # request queue

undo_stack = []    # stack to store undos


def add_request(request_id, customer_name, email, message, date, urgent=False):
    if request_id in request_ids:
        print("Error: That request ID already exists.")
        return

    # setting up the data for the customer and the request

    customer = {
        "name": customer_name,
        "email": email
    }

    request = {
        "id": request_id,
        "customer": customer,
        "message": message,
        "date": date,
        "priority": "High" if urgent else "Normal", #setting priority
        "status": "Open",
        "replies": []
    }

    requests[request_id] = request # adding to the request dictionary by id
    request_ids.add(request_id) #adding id
    request_queue.append(request_id)

    print("Support request added.")


def process_next_request():
    if not request_queue:
        print("No requests waiting.")
        return

    request_id = request_queue.popleft() # popping the stack to get the next request
    request = requests[request_id]

    print("\nProcessing request:")
    print("ID:", request["id"])
    print("Customer:", request["customer"]["name"])
    print("Priority:", request["priority"])
    print("Message:", request["message"])

    request["status"] = "In Progress"


def update_request(request_id, new_status=None, new_priority=None):
    if request_id not in requests:
        print("Request not found.")
        return

    request = requests[request_id]

    
    old_state = {
        "id": request_id,
        "status": request["status"],
        "priority": request["priority"]
    }

    undo_stack.append(old_state) # putting the old request on a stack incase we need later

    if new_status is not None:
        request["status"] = new_status

    if new_priority is not None:
        request["priority"] = new_priority

    print("Request updated.")



def undo_update():
    if not undo_stack:
        print("Nothing to undo.")
        return

    previous = undo_stack.pop() # grabbing the previous request

    #setting the request data back to the previous request
    request_id = previous["id"]

    requests[request_id]["status"] = previous["status"]
    requests[request_id]["priority"] = previous["priority"]

    print("Most recent update undone.")



def search_by_id(request_id):
    return requests.get(request_id)



def search_by_customer(name):
    results = []

    for request in requests.values():
        if request["customer"]["name"].lower() == name.lower(): # setting it lower to avoid case sensitivity
            results.append(request)

    return results


def display_request(request):
    print("\n-------------------------")
    print("Request ID:", request["id"])
    print("Customer:", request["customer"]["name"])
    print("Email:", request["customer"]["email"])
    print("Date:", request["date"])
    print("Priority:", request["priority"])
    print("Status:", request["status"])
    print("Message:", request["message"])

    print("Replies:")
    display_replies_recursive(request["replies"])

    print("-------------------------")



def display_replies_recursive(replies, index=0):
    if index >= len(replies):
        return

    print("-", replies[index])

    display_replies_recursive(replies, index + 1)


def add_reply(request_id, reply):
    if request_id not in requests:
        print("Request not found.")
        return

    requests[request_id]["replies"].append(reply)

    print("Reply added.")


def sort_requests(criteria):
    #sorting requests by criteria
    if criteria == "date":
        return sorted(requests.values(), key=lambda request: request["date"])

    elif criteria == "priority":
        priority_order = {
            "High": 0,
            "Normal": 1
        }

        return sorted(
            requests.values(),
            key=lambda request: priority_order[request["priority"]]
        )

    elif criteria == "status":
        return sorted(
            requests.values(),
            key=lambda request: request["status"]
        )

    else:
        print("Invalid sorting option.")
        return []



def display_all(request_list=None):
    if request_list is None:
        request_list = requests.values()

    for request in request_list:
        display_request(request)



def main():

    add_request(
        "R001",
        "John",
        "john@email.com",
        "My account is locked.",
        "2026-10-01",
        urgent=True
    )

    add_request(
        "R002",
        "Sarah",
        "sarah@email.com",
        "I forgot my password.",
        "2026-10-02"
    )

    add_request(
        "R003",
        "John",
        "john@email.com",
        "My order has not arrived.",
        "2026-10-03"
    )

    add_reply("R001", "We are checking your account.")
    add_reply("R001", "Your account has been unlocked.")
    add_reply("R001", "You can now log in again.")

    print("\n=== ALL REQUESTS ===")
    display_all()

    print("\n=== PROCESS QUEUE ===")
    process_next_request()

    print("\n=== UPDATE ===")
    update_request("R002", new_priority="High")

    print("\n=== UNDO ===")
    undo_update()

    print("\n=== SEARCH BY ID ===")
    result = search_by_id("R003")

    if result:
        display_request(result)

    print("\n=== SEARCH BY CUSTOMER ===")
    results = search_by_customer("John")
    display_all(results)

    print("\n=== SORT BY PRIORITY ===")
    sorted_requests = sort_requests("priority")
    display_all(sorted_requests)


if __name__ == "__main__":
    main()