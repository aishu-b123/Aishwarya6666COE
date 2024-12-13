import streamlit as st

class Bank:
    st.title('Bank Application')
    def __init__(self):
        if 'accBal' not in st.session_state:
            st.session_state.accBal = 200000
        if 'transaction_count' not in st.session_state:
            st.session_state.transaction_count = 0
        if 'count' not in st.session_state:
            st.session_state.count = 0

    def deposit(self, amount):
        if amount < 100:
            st.error("Min deposit amount is 100")
        elif amount > 50000:
            st.error("Exceeded maximum amount 50000")
        else:
            if amount % 100 != 0:
                st.error("Enter the correct amount (multiple of 100)")
            else:
                st.session_state.accBal += amount  # Update balance in session_state
                st.success(f"Successful deposit, total balance: {st.session_state.accBal}")

    def withdraw(self, amount):
        if st.session_state.transaction_count < 3:
            flag = True
            if amount > st.session_state.accBal:
                st.error("Insufficient balance")
                flag = False
            if amount < 100:
                st.error("Min amount is 100")
                flag = False
            if st.session_state.accBal - amount < 500:
                st.error("Need to maintain min 500 in account")
                flag = False
            if amount % 100 != 0:
                st.error("Enter the correct amount (multiple of 100)")
                flag = False
            if amount > 20000:
                st.error("Transaction amount limit exceeded")
                flag = False
            if flag:
                st.session_state.accBal -= amount  # Update balance in session_state
                st.session_state.transaction_count += 1  # Update transaction count
                st.success(f"Withdrawal successful, remaining balance: {st.session_state.accBal}")
        if st.session_state.transaction_count == 3:
            st.error("Transaction limit completed")

    def bal(self):
        st.write(f"Current balance: {st.session_state.accBal}")

    def show(self):
        options = {
            '1': 'Deposit',
            '2': 'Withdraw',
            '3': 'Balance Enquiry',
            '0': 'Exit'
        }

        option = st.selectbox('Select an option', list(options.values()))

        if option == 'Deposit':
            amount = st.number_input("Enter deposit amount:",step=100)
            if st.button("Deposit"):
                self.deposit(amount)
        elif option == 'Withdraw':
            amount = st.number_input("Enter withdrawal amount:",step=100)
            if st.button("Withdraw"):
                self.withdraw(amount)
        elif option == 'Balance Enquiry':
            self.bal()
        elif option == 'Exit':
            st.write("Exiting...")

    def validate(self):
        if st.session_state.count < 4:
            pin = st.number_input('Enter PIN:', step=1, key="pin_input")

            if pin == 1234:
                st.session_state.count = 0
                self.show()
            else:
                st.session_state.count += 1
                remaining_attempts = 4- st.session_state.count
                st.error(f"Invalid PIN. You have {remaining_attempts} attempts left.")
                if st.session_state.count == 4:
                    st.error("Maximum attempts reached, please try again later.")
        else:
            st.error("Maximum attempts reached, please try again later.")



ob = Bank()

ob.validate()
