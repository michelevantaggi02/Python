
from win10toast import ToastNotifier
toast = ToastNotifier()
toast.show_toast("Prova", "test", duration=100, threaded=True)
print("Qualcosa")