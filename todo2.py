import mysql.connector as mysql
 
connect = mysql.connect(host="localhost", user="root", passwd="MySQL Password")
 
cursor = connect.cursor()
 
cursor.execute("CREATE DATABASE IF NOT EXISTS TODO")
 
cursor.execute("USE TODO")
 
cursor.execute("""
    CREATE TABLE IF NOT EXISTS tb_todo (
        id INT AUTO_INCREMENT PRIMARY KEY,
        task VARCHAR(50) NOT NULL,
        status ENUM('pending', 'completed') DEFAULT 'pending'
    )
""")

print("Table created...")


while True:
    print("\n1) Insert Task")
    print("2) View Tasks")
    print("3) Update Task")
    print("4) Delete Task")
    print("5) Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        task = input("Enter task: ")
        cursor.execute("INSERT INTO tb_todo (task) VALUES (%s)", (task,))
        connect.commit()
        print("Task added.")

    elif choice == '2':
        cursor.execute("SELECT * FROM tb_todo")
        for i in cursor:
            print(i)

    elif choice == '3':
        task_id = input("Enter task ID: ")
        status = input("Enter new status (pending/completed): ")
        cursor.execute("UPDATE tb_todo SET status=%s WHERE id=%s", (status, task_id))
        connect.commit()
        print("Task updated.")

    elif choice == '4':
        task_id = input("Enter task ID: ")
        cursor.execute("DELETE FROM tb_todo WHERE id=%s", (task_id,))
        connect.commit()
        print("Task deleted.")

    elif choice == '5':
        print("Exiting...")
        break

    else:
        print("Invalid choice. Try again.")


cursor.close()
connect.close()
