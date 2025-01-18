
def extract_personalities(idx: int, result: list) -> dict:
    try:
        # 1. Openness
        O = result[0].get("openness").get("O")
        O_facet1 = result[0].get("openness").get("traits")[0].get("imagination")
        O_facet2 = result[0].get("openness").get("traits")[1].get("artistic_interests")
        O_facet3 = result[0].get("openness").get("traits")[2].get("emotionality")
        O_facet4 = result[0].get("openness").get("traits")[3].get("adventurousness")
        O_facet5 = result[0].get("openness").get("traits")[4].get("intellect")
        O_facet6 = result[0].get("openness").get("traits")[5].get("liberalism")

        # 2. Conscientiousness
        C = result[1].get("conscientiousness").get("C")
        C_facet1 = (
            result[1].get("conscientiousness").get("traits")[0].get("self_efficacy")
        )
        C_facet2 = (
            result[1].get("conscientiousness").get("traits")[1].get("orderliness")
        )
        C_facet3 = (
            result[1].get("conscientiousness").get("traits")[2].get("dutifulness")
        )
        C_facet4 = (
            result[1]
            .get("conscientiousness")
            .get("traits")[3]
            .get("achievement_striving")
        )
        C_facet5 = (
            result[1].get("conscientiousness").get("traits")[4].get("self_discipline")
        )
        C_facet6 = (
            result[1].get("conscientiousness").get("traits")[5].get("cautiousness")
        )

        # 3. Extraversion
        E = result[2].get("extraversion").get("E")
        E_facet1 = result[2].get("extraversion").get("traits")[0].get("friendliness")
        E_facet2 = result[2].get("extraversion").get("traits")[1].get("gregariousness")
        E_facet3 = result[2].get("extraversion").get("traits")[2].get("assertiveness")
        E_facet4 = result[2].get("extraversion").get("traits")[3].get("activity_level")
        E_facet5 = (
            result[2].get("extraversion").get("traits")[4].get("excitement_seeking")
        )
        E_facet6 = result[2].get("extraversion").get("traits")[5].get("cheerfulness")

        # 4. Agreeableness
        A = result[3].get("agreeableness").get("A")
        A_facet1 = result[3].get("agreeableness").get("traits")[0].get("trust")
        A_facet2 = result[3].get("agreeableness").get("traits")[1].get("morality")
        A_facet3 = result[3].get("agreeableness").get("traits")[2].get("altruism")
        A_facet4 = result[3].get("agreeableness").get("traits")[3].get("cooperation")
        A_facet5 = result[3].get("agreeableness").get("traits")[4].get("modesty")
        A_facet6 = result[3].get("agreeableness").get("traits")[5].get("sympathy")

        # 5. Neuroticism
        N = result[4].get("neuroticism").get("N")
        N_facet1 = result[4].get("neuroticism").get("traits")[0].get("anxiety")
        N_facet2 = result[4].get("neuroticism").get("traits")[1].get("anger")
        N_facet3 = result[4].get("neuroticism").get("traits")[2].get("depression")
        N_facet4 = (
            result[4].get("neuroticism").get("traits")[3].get("self_consciousness")
        )
        N_facet5 = result[4].get("neuroticism").get("traits")[4].get("immoderation")
        N_facet6 = result[4].get("neuroticism").get("traits")[5].get("vulnerability")

        return {
            "case": idx,
            "openness": O,
            "facet_imagination": O_facet1,
            "facet_artistic_interests": O_facet2,
            "facet_emotionality": O_facet3,
            "facet_adventurousness": O_facet4,
            "facet_intellect": O_facet5,
            "facet_liberalism": O_facet6,
            "conscientiousness": C,
            "facet_self_efficacy": C_facet1,
            "facet_orderliness": C_facet2,
            "facet_dutifulness": C_facet3,
            "facet_achievement_striving": C_facet4,
            "facet_self_discipline": C_facet5,
            "facet_cautiousness": C_facet6,
            "extraversion": E,
            "facet_friendliness": E_facet1,
            "facet_gregariousness": E_facet2,
            "facet_assertiveness": E_facet3,
            "facet_activity_level": E_facet4,
            "facet_excitement_seeking": E_facet5,
            "facet_cheerfulness": E_facet6,
            "agreeableness": A,
            "facet_trust": A_facet1,
            "facet_morality": A_facet2,
            "facet_altruism": A_facet3,
            "facet_cooperation": A_facet4,
            "facet_modesty": A_facet5,
            "facet_sympathy": A_facet6,
            "neuroticism": N,
            "facet_anxiety": N_facet1,
            "facet_anger": N_facet2,
            "facet_depression": N_facet3,
            "facet_self_consciousness": N_facet4,
            "facet_immoderation": N_facet5,
            "facet_vulnerability": N_facet6,
        }

    except BaseException as e:
        raise BaseException(f"Failed: {e}")
