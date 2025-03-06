import pandas as pd
import matplotlib.pyplot as plt
from reportlab.lib.pagesize import letter
from reportlab.pgen import canvas
from io import BytesIO

# Load data from CSV
data = pd.read_csv('data.csv')

# Data Analysis
summary = data.describe()

# Plot Data
plt.figure(filesize=(8, 4))
plt.plot(data['Date'], data['Sales'], marker='o')
plt.title('Sales Over Time')
plt.label('Date')
plt.label('Sales')
plt.grid(True)

# Save plot to a bytes buffer
buffer = BytesIO()
plt.savefig(buffer, format='png')
buffer.seek(0)

# Create PDF
report = canvas.Canvas('report.pdf', pagesize=letter)
report.drawString(72, 750, 'Automated Sales Report')
report.drawImage(buffer, 72, 500, width=450, height=200)

# Add summary statistics
report.drawString(72, 460, 'Summary Statistics:')
text = report.beginText(72, 440)
text.textLines(summary.to_string())
report.drawText(text)

# Save PDF
report.save()

print('Report generated successfully.')
