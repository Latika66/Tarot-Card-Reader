import random
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os

base_path = r"C:\Users\Latik\OneDrive\tarot\images"
back_image_path = os.path.join(base_path, "card_back.png")  

tarot_cards = {
    "The Fool": {
        "meaning": "Upright: New beginnings, spontaneity, innocence, and a leap of faith. The Fool represents boundless potential and a call to trust the journey ahead, even if the outcome is uncertain.\nReversed: Recklessness, naïveté, foolish decisions, or fear of stepping forward. It suggests caution in taking risks without planning.",
        "image": os.path.join(base_path, "The_Fool.png")
    },
    "The Magician": {
        "meaning": "Upright: Manifestation, resourcefulness, power, and inspired action. The Magician signifies the ability to turn dreams into reality using talents and resources.\nReversed: Manipulation, poor planning, untapped potential. It warns of misuse of power or lacking focus.",
        "image": os.path.join(base_path, "The_Magician.png")
    },
    "The High Priestess": {
        "meaning": "Upright: Intuition, mystery, subconscious wisdom, and the divine feminine. This card calls for introspection and trusting inner guidance.\nReversed: Secrets, disconnected intuition, or hidden motives. It suggests a need to reconnect with inner truths.",
        "image": os.path.join(base_path, "The_High_Priestess.png")
    },
    "The Empress": {
        "meaning": "Upright: Fertility, abundance, nurturing, and creation. The Empress symbolizes motherly care, natural growth, and creative energy.\nReversed: Dependency, creative blocks, or neglect. It may indicate a lack of self-care or stagnation.",
        "image": os.path.join(base_path, "The_Empress.png")
    },
    "The Emperor": {
        "meaning": "Upright: Authority, structure, stability, and fatherhood. The Emperor represents order, leadership, and the discipline needed to achieve goals.\nReversed: Domination, inflexibility, or lack of control. It warns against authoritarian behavior or a need to establish boundaries.",
        "image": os.path.join(base_path, "The_Emperor.png")
    },
    "The Hierophant": {
        "meaning": "Upright: Tradition, spiritual wisdom, conformity, and institutional learning. The Hierophant signifies guidance through conventional beliefs and trusted mentors.\nReversed: Non-conformity, rebellion, or questioning tradition. It suggests breaking free from outdated systems or beliefs.",
        "image": os.path.join(base_path, "The_Hierophant.png")
    },
    "The Lovers": {
        "meaning": "Upright: Love, harmony, partnerships, and values alignment. The Lovers signify meaningful relationships, choices, and unity.\nReversed: Disharmony, imbalance, or difficult decisions in relationships. It warns against ignoring personal values.",
        "image": os.path.join(base_path, "The_Lovers.png")
    },
    "The Chariot": {
        "meaning": "Upright: Determination, willpower, control, and triumph. The Chariot symbolizes overcoming challenges and staying focused on your path.\nReversed: Lack of direction, self-doubt, or loss of control. It may suggest a need to realign priorities.",
        "image": os.path.join(base_path, "The_Chariot.png")
    },
    "Strength": {
        "meaning": "Upright: Courage, inner strength, compassion, and resilience. Strength encourages patience, emotional control, and a gentle approach.\nReversed: Weakness, insecurity, or excessive force. It suggests a need to address fear or impulsive behavior.",
        "image": os.path.join(base_path, "Strength.png")
    },
    "The Hermit": {
        "meaning": "Upright: Soul-searching, introspection, solitude, and wisdom. The Hermit symbolizes a retreat to gain clarity and deeper understanding.\nReversed: Isolation, loneliness, or avoidance of self-reflection. It warns against withdrawing too much.",
        "image": os.path.join(base_path, "The_Hermit.png")
    },
    "Wheel of Fortune": {
        "meaning": "Upright: Change, luck, cycles, and destiny. This card represents life’s turning points and the influence of fate.\nReversed: Resistance to change, bad luck, or feeling stuck. It suggests taking responsibility to regain control.",
        "image": os.path.join(base_path, "Wheel_of_Fortune.png")
    },
    "Justice": {
        "meaning": "Upright: Fairness, truth, law, and accountability. Justice signifies ethical decisions and karmic balance.\nReversed: Dishonesty, unfair treatment, or lack of accountability. It warns of bias or unresolved issues.",
        "image": os.path.join(base_path, "Justice.png")
    },
    "The Hanged Man": {
        "meaning": "Upright: Surrender, perspective, letting go, and sacrifice. The Hanged Man invites acceptance of delays for greater clarity.\nReversed: Stalling, indecision, or resistance to change. It suggests a need to release outdated beliefs.",
        "image": os.path.join(base_path, "The_Hanged_Man.png")
    },
    "Death": {
        "meaning": "Upright: Endings, transformation, and new beginnings. Death signifies major transitions and the release of what no longer serves.\nReversed: Fear of change, resistance, or stagnation. It warns against clinging to the past.",
        "image": os.path.join(base_path, "Death.png")
    },
    "Temperance": {
        "meaning": "Upright: Balance, moderation, harmony, and patience. Temperance encourages blending opposites to achieve equilibrium.\nReversed: Imbalance, excess, or lack of self-control. It signals a need to restore harmony.",
        "image": os.path.join(base_path, "Temperance.png")
    },
    "The Devil": {
        "meaning": "Upright: Addiction, materialism, or feeling trapped. The Devil highlights unhealthy attachments or self-imposed limitations.\nReversed: Liberation, overcoming addiction, or reclaiming power. It signals breaking free from negative patterns.",
        "image": os.path.join(base_path, "The_Devil.png")
    },
    "The Tower": {
        "meaning": "Upright: Sudden upheaval, awakening, and chaos. The Tower symbolizes dramatic changes that bring clarity and growth.\nReversed: Avoidance of disaster or fear of change. It suggests clinging to false stability.",
        "image": os.path.join(base_path, "The_Tower.png")
    },
    "The Star": {
        "meaning": "Upright: Hope, inspiration, faith, and renewal. The Star represents healing, optimism, and alignment with purpose.\nReversed: Despair, lack of faith, or disconnection. It warns of losing hope and urges self-reconnection.",
        "image": os.path.join(base_path, "The_Star.png")
    },
    "The Moon": {
        "meaning": "Upright: Illusion, intuition, fear, and subconscious. The Moon encourages exploring hidden truths and trusting instincts.\nReversed: Clarity, release of fear, or uncovering deception. It suggests overcoming confusion.",
        "image": os.path.join(base_path, "The_Moon.png")
    },
    "The Sun": {
        "meaning": "Upright: Joy, success, positivity, and vitality. The Sun symbolizes happiness, clarity, and enlightenment.\nReversed: Temporary setbacks, overconfidence, or feeling drained. It encourages rediscovering optimism.",
        "image": os.path.join(base_path, "The_Sun.png")
    },
    "Judgement": {
        "meaning": "Upright: Rebirth, inner calling, and self-evaluation. Judgement signifies spiritual awakening and embracing higher truths.\nReversed: Self-doubt, ignoring a calling, or fear of judgment. It encourages self-reflection without fear.",
        "image": os.path.join(base_path, "Judgement.png")
    },
    "The World": {
        "meaning": "Upright: Completion, fulfillment, and wholeness. The World represents the successful conclusion of a journey and integration of lessons.\nReversed: Lack of closure, delays, or feeling incomplete. It suggests finishing what you started.",
        "image": os.path.join(base_path, "The_World.png")
    }
}

class TarotApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Tarot Card Generator")

        self.draw_button = tk.Button(master, text="Draw a Tarot Card", command=self.shuffle_animation, font=("Helvetica", 14))
        self.draw_button.pack(pady=20)

        self.card_image_label = tk.Label(master)
        self.card_image_label.pack(pady=10)

        self.meaning_label = tk.Label(master, text="", wraplength=300, justify="left", font=("Verdana", 12))
        self.meaning_label.pack(pady=10)

        self.card_images = []
        for card in tarot_cards.values():
            try:
                image = Image.open(card["image"]).resize((250, 350), Image.LANCZOS)
                self.card_images.append(ImageTk.PhotoImage(image))
            except FileNotFoundError:
                messagebox.showerror("Error", f"Image file not found: {card['image']}")
            except Exception as e:
                messagebox.showerror("Error", f"Unexpected error loading image: {e}")

        self.is_animating = False  

    def load_back_image(self):
        try:
            return ImageTk.PhotoImage(Image.open(back_image_path).resize((250, 350), Image.LANCZOS))
        except FileNotFoundError:
            messagebox.showerror("Error", f"Back image file not found: {back_image_path}")
            return None

    def draw_tarot_card(self):
        card_name = random.choice(list(tarot_cards.keys()))
        card_info = tarot_cards[card_name]

        try:
            image = Image.open(card_info["image"]).resize((250, 350), Image.LANCZOS)
            self.card_image = ImageTk.PhotoImage(image)
            self.card_image_label.config(image=self.card_image)

            upright_meaning = card_info["meaning"].split("Reversed:")[0].strip()
            reversed_meaning = card_info["meaning"].split("Reversed:")[1].strip()
            formatted_meaning = (
                f"{card_name}\n\n"
                f"Upright:\n{upright_meaning}\n\n"
                f"Reversed:\n{reversed_meaning}"
            )
            self.meaning_label.config(text=formatted_meaning)

        except FileNotFoundError:
            messagebox.showerror("Error", f"Image file not found: {card_info['image']}")
        except Exception as e:
            messagebox.showerror("Error", f"Unexpected error: {e}")

    def shuffle_animation(self):
        if self.is_animating:
            return  

        self.is_animating = True  
        def update_frame(index):
            if index < len(self.card_images):
                self.card_image_label.config(image=self.card_images[index])
                self.master.after(100, update_frame, index + 1)
            else:
                self.master.after(500, self.draw_tarot_card)  
                self.is_animating = False 

        update_frame(0)  

if __name__ == "__main__":
    root = tk.Tk()
    app = TarotApp(root)
    root.mainloop()
