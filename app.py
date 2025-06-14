from flask import Flask, render_template, request
import mysql.connector
from db_config import get_connection

app = Flask(__name__)

@app.route('/normal-signup', methods=['GET', 'POST'])
def normal_signup():
    if request.method == 'POST':
        try:
            data = (
                request.form['username'],
                request.form['password'],
                request.form['first_name'],
                request.form['last_name'],
                request.form['email']
            )
            print("📥 Form Data:", data)  # Debug print

            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO normal_users (username, password, first_name, last_name, email)
                VALUES (%s, %s, %s, %s, %s)
            """, data)
            conn.commit()
            cursor.close()
            conn.close()

            print("✅ Data inserted successfully")
            return "Normal Signup Successful!"
        except Exception as e:
            print("❌ ERROR during form submission:", str(e))  # Full error in terminal
            return "Something went wrong. Please check the server logs."
    return render_template('normal_signup.html')


@app.route('/expert-signup', methods=['GET', 'POST'])
def expert_signup():
    if request.method == 'POST':
        try:
            data = (
                request.form['username'],
                request.form['password'],
                request.form['first_name'],
                request.form['last_name'],
                request.form['email'],
                request.form['domain'],
                request.form['profession'],
                request.form['salary']
            )
            print("📥 Expert form data:", data)

            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO expert_users 
                (username, password, first_name, last_name, email, domain, profession, salary)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """, data)
            conn.commit()
            conn.close()
            print("✅ Expert user inserted!")
            return "Expert Signup Successful!"
        except Exception as e:
            print("❌ Error inserting expert user:", e)
            return "Something went wrong. Check the server logs."
    return render_template('expert_signup.html')


if __name__ == '__main__':
    app.run(debug=True)
