from fpdf import FPDF

# CUSTOMER PERSONAL DETAILS
class Invoicegenerator:
    def __init__(self):
        self.items = []
        self.sub_total = 0
        self.total_gst = 0
        self.grand_total = 0
        
        
    def customer(self):
        print("----Enter Customer Details----")
        self.name = input("Enter Name:")
        self.contact = int(input("Enter Contact:"))
        self.address = input("Enter Address:")
# PRODUCT DETAILES 
    def product(self):
        items = []
        print("---- Enter Product Details----")
        while True:
            self.product_name = input("Enter Product Name:")
            self.quantity = float(input("Enter Quantity:"))
            self.price = float(input("Enter Price:"))
            self.gst = float(input("Enter GST Rate:"))
            
            self.sub_total = self.price*self.quantity
            self.GST = (self.sub_total*self.gst)/100
            self.total_amount = (self.sub_total + self.GST)
            
            item_details = {"product_name": self.product_name,
                            "quantity":self.quantity,
                            "price":self.price,
                            "sub_total": self.sub_total,
                            "gst":self.gst,
                            "total_amount": self.total_amount,
                            "GST": self.GST
                            }
            self.items.append(item_details)
            
            choice = input("Do you want to add more items ? (Yes/No) ")
            if choice != 'Yes':
                break

# CALCULATION 
    def calculation(self):
        self.sub_total = sum(item["sub_total"] for item in self.items)
        self.total_gst = sum(item["GST"] for item in self.items)
        self.grand_total = sum(item["total_amount"] for item in self.items)
       
        
    '''def show(self):
        print("-----Bill Information-----")
        print(f'Customer Name:{self.name}')
        print(f'Contact:{self.contact}')
        print(f'Address:{self.address}')
        print(f'Product Name:{self.product_name}')
        print(f'Quantity:{self.quantity}')
        print(f'Price per pcs:{self.price}')
        print(f'Sub-Total:{self.sub_total}')
        print(f'Apply {self.gst},% GST on {self.sub_total}, is {self.GST}')
        print(f'Total Amount :{self.total_amount}')'''
        
    def generate_pdf(self):
        
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        
        pdf.cell(200, 10, text="-----Bill Information-----", ln=True, align='C')
        pdf.ln(10)
        
        pdf.cell(200, 10, text=f'Customer Name: {self.name}', ln=True)
        pdf.cell(200, 10, text=f'Contact: {self.contact}', ln=True)
        pdf.cell(200, 10, text=f'Addresse: {self.address}', ln=True)
        pdf.ln(5)
        
        # ROUGH
        '''pdf.cell(200, 10, text=f'Product Name: {self.product_name}', ln=True)
        pdf.cell(200, 10, text=f'Quantity: {self.quantity}', ln=True)
        pdf.cell(200, 10, text=f'Price: {self.price}', ln=True)
        pdf.cell(200, 10, text=f'Sub-Total: {self.sub_total}', ln=True)
        pdf.cell(200, 10, text=f'GST ({self.gst}%): {self.GST}', ln=True)
        pdf.cell(200, 10, text=f'Total Amount: {self.total_amount}', ln=True) '''
        
        # TABLE HEADER
        pdf.set_font("Arial", style="B", size=10)
        column_widths = [50,20,25,25,25,25]
        headers = ["Product", "Quantity", "Price", "Sub-Total", "GST","Total-Amount"]
        
        for i, header in enumerate(headers):
            pdf.cell(column_widths[i], 8, header, border=1, align="C")
        pdf.ln()
        
        # Table Rows
        pdf.set_font("Arial", size=10)
        for item in self.items:
            pdf.cell(column_widths[0], 8, str(item["product_name"]), border=1)
            pdf.cell(column_widths[1], 8, str(item["quantity"]), border=1, align="C")
            pdf.cell(column_widths[2], 8, f"{item['price']:.2f}", border=1, align="R")
            pdf.cell(column_widths[3], 8, f"{item['sub_total']:.2f}", border=1, align="R")
            pdf.cell(column_widths[4], 8, f"{item['GST']:.2f}", border=1, align="R")
            pdf.cell(column_widths[5], 8, f"{item['total_amount']:.2f}", border=1, align="R")
            pdf.ln()

        pdf.ln(5)
        # Summary Totals
        pdf.set_font("Arial", style="B", size=11)
        pdf.cell(200, 8, text=f"Overall Sub-Total: {self.sub_total:.2f}", ln=True, align="R")
        pdf.cell(200, 8, text=f"Total GST: {self.total_gst:.2f}", ln=True, align="R")
        pdf.cell(200, 8, text=f"Grand Total Amount: {self.grand_total:.2f}", ln=True, align="R")

        
        filename = f"Invoice_{self.name.replace(' ', '_')}.pdf"
        pdf.output(filename)
        print(f"\nSuccess! PDF Invoice saved as '{filename}'")
        

invoice = Invoicegenerator()

invoice.customer()
invoice.product()
invoice.calculation()
invoice.generate_pdf()





# ALL ITEMS KI DETAILS SHOW HO RAHI HAI AB BSS VALIDATION LAGANE HAI
