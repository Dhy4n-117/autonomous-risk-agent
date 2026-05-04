import random

topics = {
    "The Ocean": [
        "The ocean covers more than 70% of Earth's surface and remains one of the least explored frontiers on the planet.",
        "Deep-sea creatures have evolved remarkable adaptations to survive in crushing pressures and total darkness.",
        "Ocean currents act as a global conveyor belt, redistributing heat and regulating the world's climate.",
        "Coral reefs, often called the rainforests of the sea, support roughly 25% of all marine species.",
        "The Mariana Trench, the deepest point on Earth, plunges nearly 11 kilometers below the ocean surface.",
        "Bioluminescent organisms light up the deep ocean, creating an eerie, living glow in the darkness.",
        "Rising sea temperatures and acidification threaten marine ecosystems on an unprecedented scale.",
    ],
    "Artificial Intelligence": [
        "Artificial intelligence is reshaping industries at a pace that few technologies in history have matched.",
        "Machine learning models learn patterns from vast datasets, enabling them to make predictions without explicit programming.",
        "Neural networks, loosely inspired by the human brain, power everything from image recognition to language generation.",
        "Ethical questions around bias, privacy, and autonomy are central challenges facing AI researchers today.",
        "Reinforcement learning allows AI agents to master complex games and real-world control tasks through trial and error.",
        "Large language models have demonstrated surprising emergent abilities that their creators did not explicitly design.",
        "The debate over artificial general intelligence—machines that match human cognition—remains as lively as ever.",
    ],
    "Ancient Rome": [
        "At its peak, the Roman Empire stretched from the deserts of North Africa to the highlands of Scotland.",
        "Roman engineers built an extraordinary network of roads that connected the empire and facilitated trade.",
        "The Colosseum, completed in 80 AD, could hold up to 80,000 spectators for gladiatorial contests.",
        "Latin, the language of Rome, evolved into the Romance languages spoken by hundreds of millions today.",
        "Roman law formed the backbone of many modern legal systems across Europe and beyond.",
        "The city of Rome relied on a sophisticated aqueduct system to supply fresh water to its million inhabitants.",
        "The fall of the Western Roman Empire in 476 AD marked the transition from antiquity to the Middle Ages.",
    ],
    "Quantum Physics": [
        "Quantum mechanics describes the behavior of matter and energy at the smallest scales imaginable.",
        "Particles at the quantum level exist in superpositions, occupying multiple states simultaneously until observed.",
        "Quantum entanglement allows two particles to remain correlated instantaneously, regardless of the distance between them.",
        "The Heisenberg uncertainty principle states that the more precisely you know a particle's position, the less you can know its momentum.",
        "Quantum computers exploit superposition and entanglement to solve certain problems exponentially faster than classical machines.",
        "Wave-particle duality reveals that light and matter exhibit properties of both waves and particles depending on how they are measured.",
        "The double-slit experiment remains one of the most profound demonstrations of the strangeness of quantum reality.",
    ],
    "Coffee": [
        "Coffee is the second most traded commodity in the world, after crude oil.",
        "The coffee plant originated in the highlands of Ethiopia, where legend says a goat herder first noticed its stimulating effects.",
        "Espresso is not a type of bean but a brewing method that forces pressurized hot water through finely ground coffee.",
        "The caffeine in coffee works by blocking adenosine receptors in the brain, reducing the feeling of fatigue.",
        "Over 2.25 billion cups of coffee are consumed worldwide every single day.",
        "Single-origin coffees have become prized for their unique flavor profiles tied to specific regions and farms.",
        "Cold brew coffee steeps grounds in cold water for 12 to 24 hours, producing a smoother, less acidic drink.",
    ],
    "Space Exploration": [
        "Humanity's first steps beyond Earth began with Yuri Gagarin's orbit of the planet in April 1961.",
        "The Apollo program remains one of the greatest feats of engineering and human courage in recorded history.",
        "Mars has become the primary target for future crewed missions, with multiple agencies racing to send humans there.",
        "The James Webb Space Telescope can peer back over 13 billion years, capturing light from the earliest galaxies.",
        "Private companies have dramatically lowered the cost of reaching orbit, democratizing access to space.",
        "Exoplanet research has revealed thousands of worlds beyond our solar system, some potentially harboring life.",
        "The Voyager probes, launched in 1977, have now crossed into interstellar space and continue transmitting data.",
    ],
    "Music": [
        "Music is a universal human phenomenon, found in every culture across every period of recorded history.",
        "The brain's response to music involves dopamine release, the same reward pathway triggered by food and social bonding.",
        "Western music is built on a system of 12 semitones, though many traditions use microtones outside this framework.",
        "The invention of recorded sound in the late 19th century fundamentally transformed how music was consumed and shared.",
        "Jazz emerged in New Orleans in the early 20th century, blending African rhythms with European harmonic structures.",
        "Streaming platforms have shifted music economics dramatically, moving revenue from album sales to per-stream royalties.",
        "Improvisation lies at the heart of many musical traditions, from Indian classical ragas to blues guitar.",
    ],
    "Forests": [
        "Forests cover approximately 31% of the Earth's land area and are home to about 80% of terrestrial species.",
        "The Amazon rainforest produces roughly 20% of the world's oxygen and is often called the lungs of the Earth.",
        "Old-growth forests have developed over centuries, creating complex layered ecosystems that young forests cannot replicate.",
        "Trees communicate and share nutrients through underground fungal networks, sometimes called the wood wide web.",
        "Deforestation accounts for around 10% of global greenhouse gas emissions annually.",
        "Forest bathing, the Japanese practice of shinrin-yoku, has been shown to lower cortisol and boost immune function.",
        "Boreal forests, or taiga, form the largest land biome on Earth, stretching across Canada, Russia, and Scandinavia.",
    ],
}


def generate_paragraph(topic: str, sentences: list[str], num_sentences: int = 4) -> str:
    chosen = random.sample(sentences, min(num_sentences, len(sentences)))
    return " ".join(chosen)


def generate_random_paragraphs(num_paragraphs: int = 3, sentences_per_paragraph: int = 4) -> str:
    selected_topics = random.sample(list(topics.keys()), min(num_paragraphs, len(topics)))
    output = []

    for topic in selected_topics:
        paragraph = generate_paragraph(topic, topics[topic], sentences_per_paragraph)
        output.append(f"[{topic}]\n{paragraph}")

    return "\n\n".join(output)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Generate random topic paragraphs.")
    parser.add_argument("-n", "--num", type=int, default=3, help="Number of paragraphs to generate (default: 3)")
    parser.add_argument("-s", "--sentences", type=int, default=4, help="Sentences per paragraph (default: 4)")
    args = parser.parse_args()

    print("=" * 60)
    print("       RANDOM TOPIC PARAGRAPH GENERATOR")
    print("=" * 60)
    print()
    print(generate_random_paragraphs(args.num, args.sentences))
    print()
    print("=" * 60)
