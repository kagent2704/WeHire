import tkinter as tk
from tkinter import messagebox
import mysql.connector

# MySQL Connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="kashmira1234",
    database="wehire"
)
cursor = conn.cursor()

# Main Window
root = tk.Tk()
root.title("Hiring App")
root.geometry("800x600")

# Global variables for dynamic filters
location_filter = tk.StringVar()
ratings_filter = tk.StringVar()
school_level_filter = tk.StringVar()

def customer_registration():
    def register_customer():
        name = name_entry.get()
        age = age_entry.get()
        address = address_entry.get()
        phone_number = phone_entry.get()
        aadhar_number = aadhar_entry.get()
        
        query = "INSERT INTO customer (name, age, address, phone_number, aadhar_number) VALUES (%s, %s, %s, %s, %s)"
        values = (name, age, address, phone_number, aadhar_number)
        cursor.execute(query, values)
        conn.commit()
        messagebox.showinfo("Success", "Customer registered successfully!")
        customer_landing_page()

    clear_window()
    
    # GUI design matching your requirements
    tk.Label(root, text="Customer Registration", font=('Helvetica', 18, 'bold')).place(x=280, y=50)
    
    tk.Label(root, text="Name:").place(x=150, y=100)
    name_entry = tk.Entry(root, width=40)
    name_entry.place(x=280, y=100)
    
    tk.Label(root, text="Age:").place(x=150, y=140)
    age_entry = tk.Entry(root, width=40)
    age_entry.place(x=280, y=140)
    
    tk.Label(root, text="Address:").place(x=150, y=180)
    address_entry = tk.Entry(root, width=40)
    address_entry.place(x=280, y=180)
    
    tk.Label(root, text="Phone Number:").place(x=150, y=220)
    phone_entry = tk.Entry(root, width=40)
    phone_entry.place(x=280, y=220)
    
    tk.Label(root, text="Aadhar Number:").place(x=150, y=260)
    aadhar_entry = tk.Entry(root, width=40)
    aadhar_entry.place(x=280, y=260)
    
    tk.Button(root, text="Register", command=register_customer, width=15).place(x=330, y=320)

def customer_landing_page():
    def search_profession():
        profession = profession_entry.get()
        location = location_filter.get()
        ratings = ratings_filter.get()
        school_level = school_level_filter.get()
        
        # Query to fetch agencies based on filters
        query = "SELECT * FROM agency WHERE type_of_service = %s"
        filters = [profession]
        
        if location:
            query += " AND address LIKE %s"
            filters.append("%" + location + "%")
        
        if ratings:
            query += " AND ratings >= %s"
            filters.append(ratings)
        
        if profession == 'tutor' and school_level:
            query += " AND co_id IN (SELECT co_id FROM tutor_worker WHERE school_level = %s)"
            filters.append(school_level)
        
        cursor.execute(query, filters)
        results = cursor.fetchall()
        
        for agency in results:
            agency_list.insert(tk.END, agency)

    clear_window()
    
    tk.Label(root, text="Search Agencies", font=('Helvetica', 18, 'bold')).place(x=280, y=50)
    
    tk.Label(root, text="Enter Profession:").place(x=150, y=100)
    profession_entry = tk.Entry(root, width=40)
    profession_entry.place(x=280, y=100)
    
    tk.Label(root, text="Location Filter:").place(x=150, y=140)
    tk.Entry(root, textvariable=location_filter, width=40).place(x=280, y=140)
    
    tk.Label(root, text="Ratings Filter:").place(x=150, y=180)
    tk.Entry(root, textvariable=ratings_filter, width=40).place(x=280, y=180)
    
    tk.Label(root, text="School Level Filter (tutors only):").place(x=150, y=220)
    tk.Entry(root, textvariable=school_level_filter, width=40).place(x=280, y=220)
    
    tk.Button(root, text="Search", command=search_profession, width=15).place(x=330, y=260)
    
    agency_list = tk.Listbox(root, width=80, height=10)
    agency_list.place(x=100, y=320)

def agency_registration():
    def register_agency():
        name = name_entry.get()
        age = age_entry.get()
        address = address_entry.get()
        phone_number = phone_entry.get()
        aadhar_number = aadhar_entry.get()
        police_verification_status = police_status_var.get()
        type_of_service = service_type_var.get()
        mass_hiring = mass_hiring_var.get()
        ratings = ratings_entry.get()
        
        query = "INSERT INTO agency (name, age, address, phone_number, aadhar_number, police_verification_status, type_of_service, mass_hiring, ratings) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (name, age, address, phone_number, aadhar_number, police_verification_status, type_of_service, mass_hiring, ratings)
        cursor.execute(query, values)
        conn.commit()
        messagebox.showinfo("Success", "Agency registered successfully!")
        agency_landing_page()

    clear_window()
    
    tk.Label(root, text="Agency Registration", font=('Helvetica', 18, 'bold')).place(x=280, y=50)
    
    tk.Label(root, text="Name:").place(x=150, y=100)
    name_entry = tk.Entry(root, width=40)
    name_entry.place(x=280, y=100)
    
    tk.Label(root, text="Age:").place(x=150, y=140)
    age_entry = tk.Entry(root, width=40)
    age_entry.place(x=280, y=140)
    
    tk.Label(root, text="Address:").place(x=150, y=180)
    address_entry = tk.Entry(root, width=40)
    address_entry.place(x=280, y=180)
    
    tk.Label(root, text="Phone Number:").place(x=150, y=220)
    phone_entry = tk.Entry(root, width=40)
    phone_entry.place(x=280, y=220)
    
    tk.Label(root, text="Aadhar Number:").place(x=150, y=260)
    aadhar_entry = tk.Entry(root, width=40)
    aadhar_entry.place(x=280, y=260)
    
    police_status_var = tk.StringVar(value='Yes')
    tk.Label(root, text="Police Verification Status:").place(x=150, y=300)
    tk.Radiobutton(root, text="Yes", variable=police_status_var, value="Yes").place(x=280, y=300)
    tk.Radiobutton(root, text="No", variable=police_status_var, value="No").place(x=360, y=300)
    
    service_type_var = tk.StringVar(value='maid')
    tk.Label(root, text="Type of Service:").place(x=150, y=340)
    tk.OptionMenu(root, service_type_var, "maid", "nurse", "tutor", "security", "maintenance", "driver").place(x=280, y=340)
    
    mass_hiring_var = tk.StringVar(value='No')
    tk.Label(root, text="Mass Hiring:").place(x=150, y=380)
    tk.Radiobutton(root, text="Yes", variable=mass_hiring_var, value="Yes").place(x=280, y=380)
    tk.Radiobutton(root, text="No", variable=mass_hiring_var, value="No").place(x=360, y=380)
    
    tk.Label(root, text="Ratings:").place(x=150, y=420)
    ratings_entry = tk.Entry(root, width=40)
    ratings_entry.place(x=280, y=420)
    
    tk.Button(root, text="Register", command=register_agency, width=15).place(x=330, y=460)

def agency_landing_page():
    # Add Worker Function
    def add_worker():
        def perform_add_worker():
            worker_name = worker_name_entry.get()
            worker_age = worker_age_entry.get()
            worker_address = worker_address_entry.get()
            worker_phone = worker_phone_entry.get()
            worker_aadhar = worker_aadhar_entry.get()
            worker_verification_status = worker_verification_status_var.get()
            worker_wages = worker_wages_entry.get()
            worker_type = worker_type_var.get()
            agency_id = agency_id_entry.get()

            # Insert worker into the appropriate table based on the type of worker
            if worker_type == "maid":
                query = "INSERT INTO maid_worker (co_id, name, age, address, phone_number, aadhar_number, police_verification_status, wages) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            elif worker_type == "nurse":
                query = "INSERT INTO nurse_worker (co_id, name, age, address, phone_number, aadhar_number, police_verification_status, wages) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            elif worker_type == "tutor":
                school_level = school_level_var.get()
                query = "INSERT INTO tutor_worker (co_id, name, age, address, phone_number, aadhar_number, police_verification_status, wages, school_level) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            elif worker_type == "security":
                query = "INSERT INTO security_worker (co_id, name, age, address, phone_number, aadhar_number, police_verification_status, wages) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            elif worker_type == "maintenance":
                query = "INSERT INTO maintenance_worker (co_id, name, age, address, phone_number, aadhar_number, police_verification_status, wages) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            elif worker_type == "driver":
                query = "INSERT INTO driver_worker (co_id, name, age, address, phone_number, aadhar_number, police_verification_status, wages) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            else:
                messagebox.showerror("Error", "Invalid worker type selected!")
                return

            if worker_type == "tutor":
                cursor.execute(query, (agency_id, worker_name, worker_age, worker_address, worker_phone, worker_aadhar, worker_verification_status, worker_wages, school_level))
            else:
                cursor.execute(query, (agency_id, worker_name, worker_age, worker_address, worker_phone, worker_aadhar, worker_verification_status, worker_wages))
            
            conn.commit()
            messagebox.showinfo("Success", "Worker added successfully!")
            agency_landing_page()  # Redirect back to the landing page

        clear_window()
        tk.Label(root, text="Add Worker", font=('Helvetica', 18, 'bold')).place(x=280, y=50)
        
        tk.Label(root, text="Agency ID:").place(x=150, y=100)
        agency_id_entry = tk.Entry(root, width=40)
        agency_id_entry.place(x=280, y=100)

        tk.Label(root, text="Worker Name:").place(x=150, y=140)
        worker_name_entry = tk.Entry(root, width=40)
        worker_name_entry.place(x=280, y=140)

        tk.Label(root, text="Worker Age:").place(x=150, y=180)
        worker_age_entry = tk.Entry(root, width=40)
        worker_age_entry.place(x=280, y=180)

        tk.Label(root, text="Worker Address:").place(x=150, y=220)
        worker_address_entry = tk.Entry(root, width=40)
        worker_address_entry.place(x=280, y=220)

        tk.Label(root, text="Worker Phone:").place(x=150, y=260)
        worker_phone_entry = tk.Entry(root, width=40)
        worker_phone_entry.place(x=280, y=260)

        tk.Label(root, text="Aadhar Number:").place(x=150, y=300)
        worker_aadhar_entry = tk.Entry(root, width=40)
        worker_aadhar_entry.place(x=280, y=300)

        tk.Label(root, text="Police Verification Status:").place(x=150, y=340)
        worker_verification_status_var = tk.StringVar(value="Yes")
        tk.Radiobutton(root, text="Yes", variable=worker_verification_status_var, value="Yes").place(x=280, y=340)
        tk.Radiobutton(root, text="No", variable=worker_verification_status_var, value="No").place(x=340, y=340)

        tk.Label(root, text="Worker Wages:").place(x=150, y=380)
        worker_wages_entry = tk.Entry(root, width=40)
        worker_wages_entry.place(x=280, y=380)

        worker_type_var = tk.StringVar(value="maid")
        tk.Label(root, text="Worker Type:").place(x=150, y=420)
        tk.OptionMenu(root, worker_type_var, "maid", "nurse", "tutor", "security", "maintenance", "driver").place(x=280, y=420)

        school_level_var = tk.StringVar(value="elementary")
        tk.Label(root, text="School Level (tutors only):").place(x=150, y=460)
        tk.OptionMenu(root, school_level_var, "elementary", "middle", "high", "all").place(x=280, y=460)

        tk.Button(root, text="Add Worker", command=perform_add_worker, width=15).place(x=330, y=500)

    # Delete Worker Function (already completed)
    def delete_worker():
        def perform_delete_worker():
            worker_id = worker_id_entry.get()
            agency_id = agency_id_entry.get()
            worker_type = worker_type_var.get()

            if worker_type == "maid":
                query = "DELETE FROM maid_worker WHERE w_id = %s AND co_id = %s"
            elif worker_type == "nurse":
                query = "DELETE FROM nurse_worker WHERE w_id = %s AND co_id = %s"
            elif worker_type == "tutor":
                query = "DELETE FROM tutor_worker WHERE w_id = %s AND co_id = %s"
            elif worker_type == "security":
                query = "DELETE FROM security_worker WHERE w_id = %s AND co_id = %s"
            elif worker_type == "maintenance":
                query = "DELETE FROM maintenance_worker WHERE w_id = %s AND co_id = %s"
            elif worker_type == "driver":
                query = "DELETE FROM driver_worker WHERE w_id = %s AND co_id = %s"
            else:
                messagebox.showerror("Error", "Invalid worker type selected!")
                return

            cursor.execute(query, (worker_id, agency_id))
            conn.commit()

            if cursor.rowcount > 0:
                messagebox.showinfo("Success", "Worker deleted successfully!")
            else:
                messagebox.showwarning("Not Found", "No worker found with the provided details.")

            agency_landing_page()  # Redirect back to the agency's landing page

        clear_window()
        
        tk.Label(root, text="Delete Worker", font=('Helvetica', 18, 'bold')).place(x=280, y=50)
        
        tk.Label(root, text="Worker ID:").place(x=150, y=100)
        worker_id_entry = tk.Entry(root, width=40)
        worker_id_entry.place(x=280, y=100)
        
        tk.Label(root, text="Agency ID:").place(x=150, y=140)
        agency_id_entry = tk.Entry(root, width=40)
        agency_id_entry.place(x=280, y=140)
        
        worker_type_var = tk.StringVar(value='maid')
        tk.Label(root, text="Worker Type:").place(x=150, y=180)
        tk.OptionMenu(root, worker_type_var, "maid", "nurse", "tutor", "security", "maintenance", "driver").place(x=280, y=180)
        
        tk.Button(root, text="Delete Worker", command=perform_delete_worker, width=15).place(x=330, y=220)

    # Agency Landing Page Layout
    clear_window()

    tk.Label(root, text="Agency Landing Page", font=('Helvetica', 18, 'bold')).place(x=280, y=50)

    profile_frame = tk.Frame(root)
    profile_frame.place(x=100, y=100)

    tk.Label(profile_frame, text="Profile Details", font=('Helvetica', 12, 'bold')).pack()

    tk.Button(profile_frame, text="Add Worker", command=add_worker, width=20).pack(pady=10)
    tk.Button(profile_frame, text="Delete Worker", command=delete_worker, width=15).place(x=330, y=220)
    # Display list of requests and allow agency to accept or delete them
    tk.Label(profile_frame, text="Requests", font=('Helvetica', 12, 'bold')).pack(pady=10)

    request_listbox = tk.Listbox(profile_frame, width=80, height=10)
    request_listbox.pack(pady=10)

    # Function to load requests from the database
    def load_requests():
        cursor.execute("SELECT * FROM requests WHERE co_id = %s", (agency_id,))
        requests = cursor.fetchall()
        request_listbox.delete(0, tk.END)
        for req in requests:
            request_listbox.insert(tk.END, req)

    def perform_accept_request():
        selected_request = request_listbox.get(tk.ACTIVE)
        if selected_request:
            request_id = selected_request[0]
            cursor.execute("UPDATE requests SET status = 'accepted' WHERE request_id = %s", (request_id,))
            conn.commit()
            messagebox.showinfo("Success", "You have accepted the request!")
            load_requests()

    def perform_delete_request():
        selected_request = request_listbox.get(tk.ACTIVE)
        if selected_request:
            request_id = selected_request[0]
            cursor.execute("DELETE FROM requests WHERE request_id = %s", (request_id,))
            conn.commit()
            messagebox.showinfo("Success", "Request deleted successfully!")
            load_requests()

    # Buttons for accepting or deleting requests
    tk.Button(profile_frame, text="Accept Request", command=perform_accept_request, width=20).pack(pady=5)
    tk.Button(profile_frame, text="Delete Request", command=perform_delete_request, width=20).pack(pady=5)

    # Call to load the requests when the agency landing page is opened
    load_requests()

# Clear the window before loading a new page
def clear_window():
    for widget in root.winfo_children():
        widget.destroy()

# Main Menu (starting point)
def main_menu():
    clear_window()
    tk.Label(root, text="Welcome to the Hiring App", font=('Helvetica', 24, 'bold')).place(x=180, y=100)
    tk.Button(root, text="Customer Registration", command=customer_registration, width=20).place(x=280, y=200)
    tk.Button(root, text="Agency Registration", command=agency_registration, width=20).place(x=280, y=250)

# Start the app
main_menu()
root.mainloop()
