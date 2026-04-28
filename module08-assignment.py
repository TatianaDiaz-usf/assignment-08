# Module 8 Assignment: Data Lookup with Dictionaries & Basic Aggregation
# GlobalTech Solutions Customer Management System

# Welcome message
print("=" * 60)
print("GLOBALTECH SOLUTIONS - CUSTOMER MANAGEMENT SYSTEM")
print("=" * 60)

# TODO 1: Create a dictionary of service categories and hourly rates
# Store in variable: services
# Example: services = {"Web Development": 150, "Data Analysis": 175, ...}
# Include at least 5 different services
services = {"Bookkeeping": 100, "Cost accounting": 300, "Content strategy": 200, "Property management": 25, "Software development": 125}

# TODO 2: Create customer dictionaries
# Each customer should have: company_name, contact_person, email, phone
# Create at least 4 customer dictionaries
# Example: customer1 = {"company_name": "ABC Corp", "contact_person": "John Smith", ...}
customer1 = {"company_name": "Fox Corp", "contact_person": "Emily Marks", "email": "foxcorp.com", "phone": "555-1023"}
customer2 = {"company_name": "ABC Corp", "contact_person": "John Smith", "email": "abccorp.com", "phone": "813-238"}
customer3 = {"company_name": "NBC Corp", "contact_person": "Cooper Reign", "email": "nbccorp.com", "phone": "813-132"}
customer4 = {"company_name": "ESPN Inc", "contact_person": "Carter Morell", "email": "espn.com", "phone": "813-527"}

# TODO 3: Create a master customers dictionary
# Store in variable: customers
# Use customer IDs as keys and customer dictionaries as values
# Example: customers = {"C001": customer1, "C002": customer2, ...}
customers = {
    
    "C001": customer1,
    
    "C002": customer2,

    "C003": customer3,
    
    "C004": customer4
}


# TODO 4: Display all customers
print("\nAll Customers:")
print("-" * 60)
# Add your code here to display all customer information
print(customers)

# TODO 5: Look up specific customers
# Use dictionary access to:
# - Get and display customer C002's information (store in c002_info)
# - Get and display customer C003's contact person (store in c003_contact)
# - Try to get customer C999 (doesn't exist) using .get() with a default message (store in c999_info)
c002_info = customers.get("C002")
c003_contact = customers["C003"]["contact_person"]
c999_info = customers.get("C999", "Client not found")

print("\n\nCustomer Lookups:")
print("-" * 60)
# Add your code here
print(c002_info)
print(c003_contact)
print(c999_info)

# TODO 6: Update customer information
# - Change customer C001's phone number
# - Add a new field "industry" to customer C002
# - Display the updated customer information
customers["C001"]["phone"] = "813-1023"
customers["C002"]["industry"] = "Accounting"

print("\n\nUpdating Customer Information:")
print("-" * 60)
# Add your code here
print(customers)

# TODO 7: Create project dictionaries for each customer
# Each project: {"name": "Project Name", "service": "Service Type", "hours": X, "budget": Y}
# Create a projects dictionary where customer IDs map to lists of projects
# Store in variable: projects
# Example: projects = {"C001": [project1, project2], "C002": [project3], ...}
projects = {
    "C001": [{"name": "Cost solutions", "service": "Cost accounting", "hours": 50, "budget": 9000},
             {"name": "Balance", "service": "Bookkeeping", "hours": 35, "budget": 8000}],
    "C002": [{"name": "Cleaning", "service": "Property management", "hours": 10, "budget": 1000}],
    "C003": [{"name": "Content Upgrade", "service": "Content strategy", "hours": 40, "budget": 6000}],
    "C004": [{"name": "Software Upgrade", "service": "Software development", "hours": 25, "budget": 7000}]
}

print("\n\nProject Information:")
print("-" * 60)
# Add your code here
print(projects)

# TODO 8: Calculate project costs
# For each project, calculate: cost = hourly_rate * hours
# Display each project with its calculated cost
for plist in projects.values():
    for p in plist:
        rate = services[p["service"]]
        p["cost"] = rate * p["hours"]

print("\n\nProject Cost Calculations:")
print("-" * 60)
# Add your code here
print(p["name"], "-", p["cost"])

# TODO 9: Customer statistics using dictionary methods
# Display:
# - All customer IDs using .keys()
# - All customer companies using .values() and extracting company names
# - Count of total customers using len()
list(customers.keys())
list(customers.values())
(len(customers))

print("\n\nCustomer Statistics:")
print("-" * 60)
# Add your code here
print(list(customers.keys()))
print(list(customers.values()))
print(len(customers))

# TODO 10: Service usage analysis
# Create a dictionary that counts how many projects use each service
# Store in variable: service_counts
# Display the service usage counts
service_counts = {}
for plist in projects.values():
    for p in plist:
        service = p["service"]
        service_counts[service] = service_counts.get(service, 0) + 1

print("\n\nService Usage Analysis:")
print("-" * 60)
# Add your code here
print(service_counts)

# TODO 11: Financial aggregations
# Calculate and display:
# - Total hours across all projects (store in total_hours)
# - Total budget across all projects (store in total_budget)
# - Average project budget (store in avg_budget)
# - Most expensive and least expensive projects (store in max_budget, min_budget)
total_hours = [p["hours"] for plist in projects.values() for p in plist]
budget = [p["budget"] for plist in projects.values() for p in plist]
total_budget = sum(budget)
avg_budget = sum(budget) / 5
max_budget = max(budget)
min_budget = min(budget)

print("\n\nFinancial Summary:")
print("-" * 60)
# Add your code here
print("Total hours:", sum(total_hours))
print("Total budget:", total_budget)
print("Average budget:", avg_budget)
print("Max budget:", max_budget)
print("Min budget:", min_budget)

# TODO 12: Customer summary report
# For each customer, show:
# - Customer details
# - Number of projects
# - Total hours
# - Total budget
for project in projects:
    total_hours = sum(projects["hours"] for plist in projects.values() for projects in plist)
    
for project in projects:
    total_budget = sum(projects["budget"] for plist in projects.values() for projects in plist)

print("\n\nCustomer Summary Report:")
print("-" * 60)
# Add your code here
print(customers)
print(len(projects))
print(f"{project} Total hours: {total_hours}")
print(f"{project} Total budget: ${total_budget}")

# TODO 13: Create rate adjustments using dictionary comprehension
# Create a new dictionary with all service rates increased by 10%
# Store in variable: adjusted_rates
# Use dictionary comprehension: adjusted_rates = {service: rate * 1.1 for service, rate in services.items()}
adjusted_rates = {service: rate * 1.1 for service, rate in services.items()}

print("\n\nAdjusted Service Rates (10% increase):")
print("-" * 60)
# Add your code here
print(adjusted_rates)

# TODO 14: Filter customers using dictionary comprehension
# Create a dictionary of only customers who have projects
# Store in variable: active_customers
# Hint: Use the projects dictionary to check which customers have projects
active_customers = {cid: customers[cid] for cid in projects if cid in customers}

print("\n\nActive Customers (with projects):")
print("-" * 60)
# Add your code here
print(active_customers)

# TODO 15: Create project summaries using dictionary comprehension
# Create a dictionary mapping customer IDs to their total project budgets
# Store in variable: customer_budgets
# Example result: {"C001": 25000, "C002": 15000, ...}
customer_budgets ={cid: sum(p["budget"] for p in plist) for cid, plist in projects.items()}

print("\n\nCustomer Budget Totals:")
print("-" * 60)
# Add your code here
print(customer_budgets)

# TODO 16: Service pricing tiers using dictionary comprehension
# Create a dictionary categorizing services as "Premium" (>= 200), "Standard" (100-199), or "Basic" (< 100)
# Store in variable: service_tiers
# Use conditional expressions in the comprehension
service_tiers = {cid:"Premium" if services[cid] >= 200 else "Standard" if services[cid] >= 100 <=199 else "Basic" for cid in services}

print("\n\nService Pricing Tiers:")
print("-" * 60)
# Add your code here
print(service_tiers)

# TODO 17: Customer validation function
# Create a function validate_customer(customer_dict) that:
# - Checks if all required fields are present (company_name, contact_person, email, phone)
# - Returns True if valid, False otherwise
# - Use conditional logic to verify each field
# Test it on all customers and report results
def validate_customer(customer_dict):
    required = {"company_name", "contact_person", "email", "phone"}
    return required.issubset(customer_dict.keys())

print("\n\nCustomer Validation:")
print("-" * 60)
# Add your code here
for cid in customers:
    print(cid, validate_customer(customers))
  
# TODO 18: Project status tracking with loops and conditionals
# Add a "status" field to each project ("active", "completed", "pending")
# Use a loop to count projects by status
# Store counts in status_counts dictionary
# Display a summary of project statuses
active = 0
completed = 0
pending = 0
for project in customers:
    if project:
        active +=1
    if project:
        completed += 1
    if project:
        pending += 1

status_counts = {"active": active, "completed": completed, "pending": pending}

print("\n\nProject Status Summary:")
print("-" * 60)
# Add your code here
print(status_counts)

# TODO 19: Budget analysis function with aggregation
# Create a function analyze_customer_budgets(projects_dict) that:
# - Takes the projects dictionary as input
# - Uses loops to calculate total and average budget per customer
# - Returns a dictionary with customer IDs as keys and budget stats as values
# - Each value should be a dict with 'total', 'average', and 'count' keys
def analyze_customer_budgets(projects_dict):
    for project in projects:
        total_budget = (projects["budget"] for plist in projects.values() for projects in plist)
    for cid in projects.values():
        projects_dict = {"C001":"", "C002":"", "C003":"", "C004":""}
        customer_budgets = {cid: sum(p["budget"] for p in plist) for cid, plist in projects.items()}
    return projects_dict

print("\n\nDetailed Budget Analysis:")
print("-" * 60)
# Add your code here
for projects_dict in projects:
    print(analyze_customer_budgets(projects_dict))

# TODO 20: Service recommendation system
# Create a function recommend_services(customer_id, customers, projects, services) that:
# - Analyzes the customer's past projects
# - Identifies services they haven't used yet
# - Returns a list of recommended services based on their budget range
# - Use loops, conditionals, and dictionary operations
def recommend_services(customer_id, customers, projects, services):
    return (customers, projects, services)

print("\n\nService Recommendations:")
print("-" * 60)
# Add your code here
print(customers, projects, services)