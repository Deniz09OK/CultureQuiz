import json
import random
import tkinter as tk


class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CultureQuiz")
        self.root.geometry("1000x700")
        self.root.configure(bg="#2C3E50")

        self.questions = []
        self.current_question_index = 0
        self.score = 0
        self.after_id = None  # Identifiant du callback `after`

        self.show_welcome_screen()

    def show_welcome_screen(self):
        """Afficher l'écran d'accueil."""
        self.cancel_pending_actions()
        self.clear_window()

        container = tk.Frame(self.root, bg="#34495E")
        container.pack(fill="both", expand=True, padx=20, pady=20)

        welcome_label = tk.Label(
            container,
            text="Bienvenue dans le Quiz !",
            font=("Helvetica", 28, "bold"),
            fg="#ECF0F1",
            bg="#34495E",
        )
        welcome_label.pack(pady=20)

        instruction_label = tk.Label(
            container,
            text="Testez vos connaissances et amusez-vous !\nChoisissez un niveau pour commencer.",
            font=("Helvetica", 16),
            fg="#BDC3C7",
            bg="#34495E",
        )
        instruction_label.pack(pady=10)

        button_frame = tk.Frame(container, bg="#34495E")
        button_frame.pack(pady=20)

        difficulties = ["facile", "moyen", "difficile"]
        for difficulty in difficulties:
            button = tk.Button(
                button_frame,
                text=difficulty.capitalize(),
                font=("Helvetica", 16, "bold"),
                bg="#1ABC9C",
                fg="white",
                activebackground="#16A085",
                activeforeground="white",
                cursor="hand2",
                command=lambda diff=difficulty: self.start_quiz(diff),
            )
            button.pack(padx=10, pady=5, ipadx=20, ipady=10)

    def start_quiz(self, difficulty):
        """Démarrer le quiz."""
        self.cancel_pending_actions()
        self.current_question_index = 0
        self.score = 0
        self.difficulty = difficulty
        self.questions = load_questions_from_json("questions.json", difficulty, num_questions=10)
        self.clear_window()
        self.create_quiz_interface()
        self.load_question()

    def create_quiz_interface(self):
        """Créer l'interface utilisateur du quiz."""
        self.container = tk.Frame(self.root, bg="#2C3E50")
        self.container.pack(fill="both", expand=True, padx=20, pady=20)

        top_frame = tk.Frame(self.container, bg="#2C3E50")
        top_frame.pack(fill="x", pady=10)

        self.progress_label = tk.Label(
            top_frame,
            text="",
            font=("Helvetica", 18, "bold"),
            fg="#ECF0F1",
            bg="#2C3E50",
        )
        self.progress_label.pack(side="left", padx=20)

        change_level_button = tk.Button(
            top_frame,
            text="Changer de niveau",
            font=("Helvetica", 14, "bold"),
            bg="#E74C3C",
            fg="white",
            activebackground="#C0392B",
            activeforeground="white",
            cursor="hand2",
            command=self.show_welcome_screen,
        )
        change_level_button.pack(side="right", padx=20)

        self.question_label = tk.Label(
            self.container,
            text="",
            font=("Helvetica", 20, "bold"),
            fg="#F1C40F",
            bg="#2C3E50",
            wraplength=800,
            justify="left",
        )
        self.question_label.pack(pady=20)

        self.option_buttons = []
        for i in range(4):
            btn = tk.Button(
                self.container,
                text="",
                font=("Helvetica", 16),
                bg="#3498DB",
                fg="white",
                activebackground="#2980B9",
                activeforeground="white",
                cursor="hand2",
                command=lambda i=i: self.check_answer(i),
            )
            btn.pack(fill="x", pady=10, ipadx=10, ipady=10)
            self.option_buttons.append(btn)

        self.feedback_label = tk.Label(
            self.container,
            text="",
            font=("Helvetica", 16),
            fg="#E74C3C",
            bg="#2C3E50",
        )
        self.feedback_label.pack(pady=20)

    def load_question(self):
        """Charger une nouvelle question."""
        question_data = self.questions[self.current_question_index]
        self.progress_label.config(
            text=f"Question {self.current_question_index + 1}/{len(self.questions)}"
        )
        self.question_label.config(text=question_data["question"])

        for i, option in enumerate(question_data["options"]):
            self.option_buttons[i].config(text=option, state=tk.NORMAL, bg="#3498DB")

        self.feedback_label.config(text="")

    def check_answer(self, selected_index):
        """Vérifier la réponse sélectionnée."""
        question_data = self.questions[self.current_question_index]
        correct_answer = question_data["answer"]

        if question_data["options"][selected_index] == correct_answer:
            self.score += 1
            self.feedback_label.config(text="Bonne réponse !", fg="#2ECC71")
        else:
            self.feedback_label.config(
                text=f"Mauvaise réponse ! La bonne réponse était : {correct_answer}.",
                fg="#E74C3C",
            )

        for btn in self.option_buttons:
            btn.config(state=tk.DISABLED)

        self.current_question_index += 1
        self.after_id = self.root.after(2000, self.load_next_or_end)

    def load_next_or_end(self):
        """Passer à la question suivante ou terminer le quiz."""
        if self.current_question_index < len(self.questions):
            self.load_question()
        else:
            self.show_final_score()

    def show_final_score(self):
        """Afficher le score final."""
        self.clear_window()
        final_score_label = tk.Label(
            self.root,
            text=f"Quiz terminé ! Votre score : {self.score}/{len(self.questions)}",
            font=("Helvetica", 24, "bold"),
            fg="#F1C40F",
            bg="#2C3E50",
        )
        final_score_label.pack(pady=30)

        restart_button = tk.Button(
            self.root,
            text="Rejouer",
            font=("Helvetica", 16),
            bg="#1ABC9C",
            fg="white",
            activebackground="#16A085",
            activeforeground="white",
            cursor="hand2",
            command=self.show_welcome_screen,
        )
        restart_button.pack(pady=10, ipadx=20, ipady=10)

    def cancel_pending_actions(self):
        """Annuler les actions en attente."""
        if self.after_id is not None:
            self.root.after_cancel(self.after_id)
            self.after_id = None

    def clear_window(self):
        """Supprimer tous les widgets de la fenêtre."""
        for widget in self.root.winfo_children():
            widget.destroy()


def load_questions_from_json(file_path, difficulty, num_questions=10):
    """Charger les questions depuis un fichier JSON."""
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return random.sample(data[difficulty], num_questions)


if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
