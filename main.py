from graph import graph


def main():
    while True:
        print("\n" + "=" * 60)

        question = input("IELTS Question (type 'exit' to quit):\n> ")

        if question.lower() == "exit":
            break

        state = {
            "user_prompt": question,
            "essay": "",
            "feedback": "",
            "attempt_count": 1,
            "decision": "",
        }

        print("\nStarting Reflection Agent...\n")

        final_state = None

        for event in graph.stream(state):
            for node_name, node_state in event.items():

                if node_name == "writer":
                    if node_state["attempt_count"] == 1:
                        print("Writing essay...")
                    else:
                        print(f"Rewriting essay (Attempt {node_state['attempt_count']})...")

                elif node_name == "checker":
                    print("Checking essay...")

                    if node_state["decision"] == "PASS":
                        print("PASS")
                    else:
                        print("FAIL")
                        print(node_state["feedback"])
                        print()

                final_state = node_state

        print("\n" + "=" * 60)
        print("FINAL ESSAY")
        print("=" * 60)
        print(final_state["essay"][0]['text'])

        print("\nAttempts:", final_state["attempt_count"])
        print("Decision:", final_state["decision"])


if __name__ == "__main__":
    main()