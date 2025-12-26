import matplotlib.pyplot as plt


def plot_sanctioned_vs_completed(yearly_df):
    plt.figure()
    plt.plot(yearly_df["year"], yearly_df["TOT_LEN"], label="Sanctioned Length")
    plt.plot(yearly_df["year"], yearly_df["CCTOT_LEN"], label="Completed Length")
    plt.xlabel("Year")
    plt.ylabel("Road Length (km)")
    plt.title("PMGSY Road Length: Sanctioned vs Completed (Maharashtra)")
    plt.legend()
    plt.show()


def plot_length_completion_rate(yearly_df):
    plt.figure()
    plt.plot(yearly_df["year"], yearly_df["length_completion_rate"])
    plt.xlabel("Year")
    plt.ylabel("Completion Rate (%)")
    plt.title("Road Length Completion Rate (Maharashtra)")
    plt.show()


def plot_spend_realization_rate(yearly_df):
    plt.figure()
    plt.plot(yearly_df["year"], yearly_df["spend_realization_rate"])
    plt.xlabel("Year")
    plt.ylabel("Spend Realization Rate (%)")
    plt.title("PMGSY Spend Realization Rate (Maharashtra)")
    plt.show()


def plot_completion_by_sanction_year(sanction_year_df):
    plt.figure()
    plt.bar(
        sanction_year_df["sanction_year"],
        sanction_year_df["length_completion_rate"]
    )
    plt.xticks(rotation=90)
    plt.xlabel("Sanction Year")
    plt.ylabel("Completion Rate (%)")
    plt.title("Completion Rate by Sanction Year (Maharashtra)")
    plt.show()