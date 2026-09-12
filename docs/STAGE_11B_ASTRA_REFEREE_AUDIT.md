# Stage 11B — Independent Hostile Referee Audit

監査日：2026-09-12。対象：*Dynamic Tariff Choice for Generative AI: Model Improvement, Commitment, and Welfare*。

- Theory freeze: `2597e82044ec94a58fad033227ea415e64af8c6d`
- Manuscript: `c6325c169efaeac14fe9c563281fee5252940255`
- Workflow: `ryotamatsuki/research-paper-workflow`、GOVERNANCE、Stage 11 / 4A templates。
- 独立性：別のStage 11 report / repair / verdictは読んでいない。指定commitの原稿・freeze registersを読み、production Python / Leanを読む前に独立の直接利潤評価コードを作成・実行した。その後に既存コード、Lean signatures、許可された歴史的Stage 4A / 7 / 7.5A記録を照合した。
- 「Referee A–D」は本監査内の四つの評価視点であり、四人の独立したエージェントによる投票ではない。ファイル名は指定どおりであり、モデル間の合意を意味しない。
- 原稿、既存production verification、Lean、freeze registersは変更していない。以下の数式導出は監査証拠であり、凍結定理への無断追加ではない。
- 独立コード：`verification/stage11b_astra_independent.py`。結果：`verification/stage11b_astra_results.json`。実行：`python verification/stage11b_astra_independent.py`（numpy/scipy）。

## 1. Executive verdict

**REOPEN EARLIER STAGE / NO-GO**

主因はbaseline T1–T3の反証ではなく、**Stage 7.5AのCDFロバストネス証拠におけるactive-set認証の失敗**である。既存の `G(z)=sqrt(z)` 例は、flat予想状態でH-onlyが両タイプ供給より厳密に高利潤となる。したがって、その例で計算された「flat-induced state」は、全料金を再最適化する経済ゲームの状態ではない。単なる数値精度の問題ではない。

他方、凍結された二次効用・一様分布・strict Rのもとでは、次を独立に確認した。

1. 継続料金の大域的active-set比較から、両タイプ供給の価格式、利潤差、閾値分離を再導出できる。
2. preferred candidates以外のH-only / L-only / no-service / cutoff / zero-profitを検討しても、strict R内で追加の実質的な均衡結果は見つからない。後述の排除論証は候補検算とは別である。
3. strict gap内の混合**結果**は一意。ただし、測度ゼロの個別行動や到達しない履歴での戦略まで一意ではない。
4. 固定導入量の厚生恒等式は正しく、内生導入量のarchitecture-commitment厚生は同一の正則パラメータ族で符号が反転する。
5. 閾値分離が既存論文にそのまま包含される証拠は今回得られなかった。しかし、そのことはIJIO/JIE級の貢献認定ではない。

**最初に差し戻す対象はStage 7.5A。** baseline Stage 4の式を修正する根拠は得られていない。CDF例の経済的証拠分類を訂正・再認証し、Stage 8を再確認する。一般CDFの均衡を新たに拡張して救済することは本監査では行わない。

## 2. Top 5 rejection risks

| 順位 | リスク | 判定 | 何が問題か |
|---|---|---|---|
| 1 | CDFロバストネスの大域最適性が未成立 | MAJOR BUT FIXABLE / CERTIFICATION REGRESSION | sqrt例はR外。偽のflat状態・偽の利潤差を経済的頑健性の証拠として扱えない。 |
| 2 | 新規性の増分が小さく、比較が未更新 | MAJOR BUT FIXABLE | Min–Ryu、Wang–Hu、Ladas等との明示的比較不足。Bergemann–Bonatti–Smolinの2026改訂版が未反映。 |
| 3 | Rと均衡集合の説明が暗黙的 | MAJOR BUT FIXABLE（証明補足で対応可能） | 経済的に重要な制限を「globally optimal」と定義するだけ。候補以外の状態を排除する論証が原稿にない。独立監査では排除できた。 |
| 4 | AI制度への接続が弱い | MAJOR BUT FIXABLE（投稿先・解釈の問題） | 既にメータリングする企業の追加的固定費μ、企業単位の契約とtask単位の固定料の対応が未説明。事実誤認を立証したわけではない。 |
| 5 | 題名とモデル改善の実質が不一致 | MINOR（ただしeditorialに目立つ） | qualityの状態変数・遷移・投資はない。モデル改善は条件付き解釈に留まる。 |

FATALなbaseline反例を発見した、とは報告しない。主定理を反証していないのに「致命的な数式誤り」と呼ぶことは敵対的監査ではなく過剰判定である。

## 3. Referee A — novelty / mechanism

最も強い攻撃は、数学的な誤りより**既知の非コミットメント問題を非常に小さな二択モデルで再表示しているだけではないか**という点である。T2はT1と単調性の即時系であり、T3の混合確率は標準的な無差別条件と導入条件から得られる。これらを別々の新しい理論貢献として加算できない。

残り得る貢献は、匿名二部料金を事後的に再最適化する経済環境から、利用者側と供給者側に逆向きの反応を同時に導き、期待に依存する二つの閾値を構成したこと。適用対象がAIであること自体は貢献ではない。

匿名・単一料金の制約は本質的である。タイプ別の完全抽出を許すと継続レントが変わる。この点はMin–Ryuの価格差別と投資の議論に近い。現在の論文は匿名性を明示しているので、禁止されたメニューへの逸脱を「baselineの反例」とする攻撃はFALSE POSITIVE。ただし、なぜこの契約制限が対象市場で重要なのかは査読上の問いとして残る。

**A1**

- Attack → 閾値分離は既存hold-up / tariff-choiceの言い換えか。
- Severity → MAJOR BUT FIXABLE（増分の評価）。全ゲーム包含は未立証。
- Exact evidence → `sections/07_related_literature.tex`、`references/*.bib`にMin–Ryu、Wang–Hu、Ladasの明示的比較がなく、BBSは2025年版のみ。§15の一次資料照合。
- Mathematical/economic consequence → T1–T3の正しさから、重要性やIJIO適合性は導けない。
- Can the paper answer now? → 一部。凍結された狭い主張は区別可能だが、現稿の比較表・最新版照合は不足。
- Required fix → 全ゲームのtiming / action / state / payoffを比較し、重複を明示。応用先の差を独立の新規性として数えない。
- Earliest affected stage → Stage 6のnovelty ledger / Stage 10 literature exposition。
- Certification regression? → NO（既存の主定理包含を今回立証したわけではない）。

## 4. Referee B — mathematical validity / equilibrium set

baselineの式は独立再導出に耐えた。ただし現稿のappendixは両タイプ供給のFOC/SOCと二候補の比較が中心であり、H-only、no-service、無差別な参加行動の全体を読者が追える形にはなっていない。

本監査の§7–12では、まず任意料金の参加セルから大域候補を導き、次に均衡状態が存在し得る区間を制限した。この二段階が重要である。Rでcandidateが大域最適でも、その事実だけで別の導入状態の均衡は排除されない。

**B1**

- Attack → Rの暗黙的定義が、候補検証を均衡集合の認証に見せていないか。
- Severity → MAJOR BUT FIXABLE（証明・定義の明示不足）。baseline false theoremではない。
- Exact evidence → `sections/02_model.tex`, subsection “The regular both-served region”; `sections/10_appendix.tex`, T3 proof; 歴史的Stage 4A §5のalternative-equilibrium欄は二候補と単調性の列挙。
- Mathematical/economic consequence → その記述だけでは低導入状態のH-only等の排除を読者が検証できない。
- Can the paper answer now? → YES。§7–9の大域候補・単調なactive-set利潤差・状態区間論証で回答可能。
- Required fix → 新しい仮定を加えず、Rのstrictな利潤差と候補以外の排除論証を証明に記録する。「unique」は結果の一意性と明記。
- Earliest affected stage → Stage 10の証明説明。定理の範囲を変更するならchange control。
- Certification regression? → NO（独立監査で主張の失敗は確認されず、欠けた論証を構成できた）。

**B2：確定した認証回帰**

- Attack → 一般CDF例でも全料金を再最適化しているか。
- Severity → MAJOR BUT FIXABLE / **CERTIFICATION REGRESSION**。
- Exact evidence → `verification/robustness_checks.py::cdf_checks` のsqrt例、歴史的 `dynamic-tariff-choice-generative-ai-stage075a-report.md` §3 / §6、§13の独立計算。flat状態 `sqrt(5/8)` ではH-only優位が `0.3575623676894266`。
- Mathematical/economic consequence → 同例の `h_F` は実際のflat継続最適化と両立しない。正しい大域利潤差は `1.4247622748300728`、両タイプ式は `1.7823246425195`。抽象定理の経済的前提の例証になっていない。
- Can the paper answer now? → NO、現在の「checks confirm」のままでは不可。あくまで仮定されたレント写像の固定点を検算しただけ、と分類すれば数値自体は正しい。
- Required fix → sqrt例を全ゲーム頑健性のpositive evidenceから外し、active-set失敗のnegative recordとして残す。各例に大域料金・参加集合の証拠を添える。production codeは本監査で変更していない。
- Earliest affected stage → **Stage 7.5A**。変更したCDF下の継続問題は同stageで再認証。
- Certification regression? → **YES**。一般性テストで変えた分布が導入状態をR外へ動かさないか、再検証するcheckが不足。

## 5. Referee C — welfare / benchmark / institution

厚生の三つの対象は現稿で正しく区別されている。支払額を厚生から除外すること、integration costを導入した利用者にだけ計上すること、μを実物費用として一度だけ引くことは妥当である。first bestは直接数量を選ぶplannerであり、metered contractを使う必要がないというchoice setが歴史的Stage 7にも明記されている。

固定導入量のW1から「meteringを禁止すべき」という結論は出ない。現稿もその結論を述べていない。独立の符号反転例は§14。

**C1**

- Attack → 実際のenterprise/cloud契約を `p=0` 対 `p>0` と同一視し、導入が料金変更を引き起こす事実があるかのように扱っていないか。
- Severity → MAJOR BUT FIXABLE（制度的動機の説得力）。事実と解釈の分離自体は概ねPASS。
- Exact evidence → `sections/06_institutional.tex`、§15のOpenAI/AWS一次資料。利用枠・クレジット・超過課金・事前の支出コミットメントが存在する。
- Mathematical/economic consequence → 契約併存は動学的因果機構の証拠ではない。実際の固定枠の限界価格は全利用量でゼロではない。すでに利用量を測っているproviderのμは技術導入費と当然には同一でない。
- Can the paper answer now? → 限定的。現稿はtheoretical interpretationと明記しているが、μの実務的な発生単位・契約更新時点が未特定。
- Required fix → 事実／示唆／モデル解釈を分離した短い表を置き、μを未識別の実物費用と明記。企業が複数taskを束ねて契約する場合と、モデルのtask単位固定料との差も示す。
- Earliest affected stage → Stage 7 institution / Stage 10 exposition。
- Certification regression? → NO。因果的な制度事実を断定したとの反証ではない。

## 6. Referee D — exposition / journal fit / claim scope

モデルの改善は `a_L,a_H` の解釈でしかなく、quality improvementを変数として最適化・遷移させていない。題名の“Model Improvement”は、読者に実際より大きな内容を期待させる。時間整合性のあるtariff選択問題という中心に題名を合わせる方が正確だが、本監査では変更しない。

「二つの閾値」があることは独立した深い定理ではなく、構造的な導出の帰結である。T1、T2、T3、collapseを多数の貢献として提示すると、水増しと評価され得る。一方、本文はmixed strategies自体を新規性としない点で抑制されている。

**D1**

- Attack → 題名の改善・動学性と実際の経済内容が一致するか。
- Severity → MINOR（editorial riskは残る）。
- Exact evidence → `sections/06_institutional.tex` 最終段落、`sections/08_discussion.tex` “Comparative implications”。任意の品質変化に対する閾値単調性を証明していないと明記。
- Mathematical/economic consequence → quality-led tariff lifecycleは定理ではない。
- Can the paper answer now? → YES、限定は本文にある。
- Required fix → 題名・abstract・導入で同じ期待値を設定する。quality extensionを追加して救済しない。
- Earliest affected stage → Stage 10。
- Certification regression? → NO。

IJIO/JIE適合性は、正しい式があることとは別問題である。現状の論文には、狭い実装を超える新しい一般定理や、制度に固有な比較静学の強い結果はない。拒否理由は「単純だから」ではなく、単純なモデルで得た結果が既知のcommitment分析に比べ何を新しく説明するかの立証不足である。

## 7. Primitive re-derivation of continuation pricing

以下 `a=a_L`, `a_H=a+d`, `n=l+h`, `A=a-c` と置く。`F`の符号は現稿で明示されていないが、負のFを許してもbaseline最適値は変わらない：`S_j(p)>=0`なので負の固定料をゼロに上げることは収入を弱く改善する。

### 7.1 Usage and participation

参加後に `max_{q>=0} (a_j-p)q-q²/2` を解くと

\[
q_j(p)=(a_j-p)_+,\qquad S_j(p)=\tfrac12(a_j-p)_+^2.
\]

参加は `S_j(p)-F>=0`。`p<a_H`かつHに正の数量がある場合、Lが正の数量で参加できる料金でHを厳密に排除できない。

固定pで利潤は各参加セル上でFについて線形かつ増加する。従って有限の正の導入量があれば調べるべき上端は `F=S_L(p)`, `F=S_H(p)` とno-service。`F=0`も価格のchoke境界として明示的に検査する。L-onlyはHの厳密な参加誘因に反する。`p>=a_H,F=0`で任意の参加行動が可能でも、数量・収入はゼロである。

### 7.2 Both served

`0<=p<=a`で `F=(a-p)²/2` を代入すると

\[
B(p)=n(a-p)^2/2+(p-c)\{l(a-p)+h(a+d-p)\}.
\]

平方完成すると

\[
B(p)=B(0)+(nc+dh)p-np^2/2
=B(0)+\frac{(nc+dh)^2}{2n}-\frac n2(p-c-dh/n)^2.
\]

従ってSOCは `-n<0`、内点候補は

\[
\bar p=c+dh/n.
\]

`0<bar p<a`ならこれが枝上の一意な最大。`bar p>=a`なら枝の最大は `p=a,F=0`。strict Rでは後者を排除する必要がある。`p=0`はflatに含まれ、meteredの集合には含まれないが、極限の比較にも使える。

### 7.3 H-only

H-onlyの最適固定料は `F=S_H(p)`。粗利潤は

\[
H(p)=h\{S_H(p)+(p-c)q_H(p)\}
=\frac h2\{(a+d-c)^2-(p-c)^2\},\quad p<a+d.
\]

従ってmetered H-onlyでは `p=c`, `F=(a+d-c)²/2`, 利潤 `H_M=h(a+d-c)²/2`。Hは継続レントゼロ、Lは排除される。これはFOCだけでなく平方差から大域最大である。

flat H-onlyでは `p=0`, `F=(a+d)²/2`, 利潤 `H_F=h((a+d)²/2-c(a+d))`。これが負ならno-serviceが優位。

### 7.4 Global envelope and boundaries

\[
V_F=\max\{B_F,H_F,0\},\quad B_F=B(0),
\]

\[
V_M=\max\{B(\min\{\bar p,a\}),H_M,0\}.
\]

`V_M`はμを引く前。architecture選択は **`V_M-mu` と `V_F`** の比較である。μは両方のmetered active setsで共通なので、その内部順位を変えない。

`p>=a,F=0`の正のH需要はH-onlyの資源余剰を超えられず、`H_M`に支配される。`p>=a+d`はzero-demand。`F=0,p<a`は参加セル上の固定料増額に支配される。`p=0,F=0`はstrict Rでは正の固定料に支配される。従ってstrict R内では取り逃したF=0 / participation-price boundary / zero-service最適解はない。

### 7.5 R can be expressed without an optimizer oracle

両タイプ供給とH-onlyの差は

\[
D_F(h)=B_F-H_F=l\,a(a/2-c)-hR_F,
\]

\[
D_M(h)=B_M-H_M=\frac l2(a-c)^2-hd(a-c)-\frac{d^2lh}{2(l+h)}.
\]

\[
D_F'=-R_F<0,\qquad D_M'=-d(a-c)-\frac{d^2l^2}{2(l+h)^2}<0.
\]

さらに内点式の差を整理すると

\[
D_M-D_F=lc^2/2+hdc+\frac{d^2h^2}{2(l+h)}>0.
\]

従って `D_F(h_F)>0` は `a>2c`を含意し、meteredの両タイプ優位も含意する。`bar p>=a`なら上の形式的 `D_M<0`となるので内点条件にも反する。よってbaselineでは、その他のprimitive interiority条件に加えて

\[
l\,a(a/2-c)>h_FR_F
\]

というstrictな不等式が、全区間のactive-set条件を確認する具体的な方法となる。これは新たな仮定の後付けではなく、凍結された大域両タイプ供給条件を展開したもの。

正則例の上端での厳密な余裕は `D_F(h_F)=31/80`、`D_M(h_F)=3533/2280`。したがって正則集合は空でもknife-edgeでもない。

### 7.6 Metering gain

両方の大域最適解がBの場合のみ、平方完成から

\[
\Phi=V_M-V_F=\frac{(nc+dh)^2}{2n}.
\]

\[
\Phi_h=\frac{(cn+dh)(cn+dh+2dl)}{2n^2}>0
\]

は `c>0,d>0,l>0,h>=0`で成立する。式の正値性と、「その式が大域利潤差であること」は別の証明義務である。active setが変わった後の正しい対象は `V_M-V_F`。

## 8. Candidate-deviation re-audit

Lは継続レントゼロなので `l=b_L/K_L`。Hのflatレントは `R_F`、meteredレントは `R_F-dp`。

\[
h_F=(b_H+R_F)/K_H,\quad
K_Hh_M=b_H+R_F-dc-d^2h_M/(l+h_M).
\]

`C=b_H+R_F-dc>0`と置くと

\[
K_Hh^2+(K_Hl+d^2-C)h-Cl=0.
\]

定数項が負なので正根は一つ。`g(h)=C-d²h/(l+h)-K_Hh`について、`g(0)>0`, `g(h_F)<0`, `g'<0`である。必要な正確な制約は `K_H>0,l>0,c>0,d>0`, `dc<b_H+R_F<K_H`と、使用する全状態での料金枝の大域最適性。`0<h_M<h_F<1`が成立する。

恒等式自体を反復実行するのではなく、独立コードでは効用から得た最大化料金のHレントを使って導入固定点を解いた。

| 独立計算 | 値 |
|---|---:|
| `h_M` | 0.4547003097 |
| `h_F` | 0.625 |
| `mu_M` | 1.1644416021 |
| `mu_F` | 1.4745614035 |
| `mu` | 1.3 |
| flat期待状態でmeteringへ逸脱する純利得 | 0.1745614035 |
| metered期待状態でflatへ逸脱する純利得 | 0.1355583979 |
| `h*` | 0.5296693311 |
| `rho*` | 0.5453907723 |

最適化誤差により閉形式との末尾桁はわずかに異なる。定理はこの数値例で認定したのではなく、§7の大域比較と上記符号論証による。

## 9. Alternative-equilibrium search

候補に対する逸脱検査とは別に、以下を行った。

**状態の排除論証。** すべての均衡で各classは `b_j>0`から正の導入量を持つ。大域最適な料金でLのレントはゼロ。Hのレントは、Bなら `[0,R_F]`、H-only / no-serviceならゼロである。従って

\[
l=b_L/K_L,\qquad h\in[h_0,h_F],\qquad h_0=b_H/K_H>0.
\]

strict Rの上端で `D_F,D_M>0`なら、それらがhについて減少するため、より低い `h_0`まで両タイプ供給が厳密に優位。これにより、Rのcandidate intervalより下に隠れたH-only均衡を排除できる。H-onlyを仮定した導入量 `h=h_0`でproviderがH-onlyを最適に選ばないためである。

| 探索したprofile | strict Rでの結論 | 別の経済結果を生むか |
|---|---|---|
| H-only flat / metered | `h_0`に戻り、両タイプ供給へ厳密に逸脱 | NO |
| L-only | 正需要のHがより高いsurplusを得るためH排除不能 | NO |
| no integration | `k<b_j`の正の測度が導入に逸脱 | NO |
| full integration | 継続レント上限と `h_F<1,l<1`に反する | NO |
| no-service | strict Rでは正の供給利潤に劣る | NO |
| zero provider profit | strict Rでproviderの最適値は正 | NO |
| F=0 / p=0 / choke price | §7の大域候補と境界比較で処理 | NO |
| classごとのintegration cutoff上の利用者 | 一様分布で測度ゼロ | aggregate outcomeは不変 |
| providerがarchitectureに無差別 | integration条件で混合確率が決まる | §12 |

コードは `h_0,h_M,h_F,0,1`の別候補を各architectureで検査し、さらに501状態の大域active-set sweepを保存する。表の普遍的な排除は数値グリッドでなく上の解析による。

全経済が空のoff-path historyでは多くの料金が利潤ゼロになる。この戦略的非一意性を捨てていない。ただしatomlessな単独導入は総量を変えず、strict Rの正の導入量の結果を別の均衡結果へ変えるものではない。

## 10. Boundary / active-set / H-only audit

### 10.1 Exact 23/10 guard

`a=4,d=1,c=1,l=1/10,h=3/5`で、直接の収入−費用から `B_F=11/5`, `H_F=9/2`、差は厳密に `23/10`。これは既存スクリプトを呼ばず `Fraction` で確認した。

### 10.2 Rの近傍で真のgainが反転

`a=4,d=1,c=1,l=4/5`のままhを増やす。flatのactive-set境界は

\[
h_B=\frac{l\,a(a/2-c)}{R_F}=\frac{32}{45}.
\]

境界の左では両architectureともB。右の近傍ではflatがH-only、meteredはB。従って

\[
\Psi(h)=V_M-V_F=\Phi(h)+D_F(h),\quad h>h_B\text{ の近傍}.
\]

その導関数は `Phi_h-R_F<0`（この例）。`Phi_h>0`という式だけを見て大域gainの単調性を主張すると、符号を誤る。

| h | flat optimum | metered optimum | 大域gain |
|---:|---|---|---:|
| 0.710 | B | B | 1.6319205298 |
| 0.712 | H-only | B | 1.6316402116 |
| 0.800 | H-only | B | 1.4000000000 |
| 1.000 | H-only | B | 0.8777777778 |

### 10.3 Rの直外にある追加のpure-architecture equilibrium

一様分布を維持し、正則例から `K_H=7`だけに変える。`h_F=5/7`は `32/45`をわずかに超える。`mu=1637/1000`とする。

導入状態 `l=4/5,h=32/45`でproviderは必ずflatを選び、料金を

\[
(p,F)=(0,8)\ \text{with probability }\lambda=403/405,
\]

残りの確率で `(p,F)=(0,25/2)` とする。参加制約に等号の利用者は参加する。

- 両flat料金の利潤はともに `16/3`。他のflat料金は上回らない。
- meteredの大域粗利潤差は `250/153 < 1637/1000`。従ってmeteredへの逸脱は不利。
- Lの継続レントは常にゼロ、よって `l=4/5`。
- Hの期待レントは `(403/405)(9/2)`。
- `1/2+(403/405)(9/2)=7(32/45)`なのでHの導入も整合する。

一方、両タイプ式を無効な上端まで延長すると `Phi(h_F)=3042/1855`で、`250/153 < 1637/1000 < 3042/1855`。つまり、無効なbranchの「gap」に見える領域で、実際にはarchitectureを混合しない均衡が存在する。

これは**純粋な全行動戦略均衡ではなく、料金額を混合するpure-architecture equilibrium**である。この区別を明示する。providerの等利潤な料金行動が利用者レントを変えるため、捨ててはいけない例である。

影響：strict RのT3は反証しない。outside-Rまで拡張したno-pure-regime statementは反証する。outside-Rのmixed-architecture uniquenessや単一料金に基づく厚生値もそのまま使えない。本文のR限定を外せない経済的理由が明確になる。

## 11. Indifference and multiplicity audit

**参加の無差別。** BではLが無差別だが、strict Rの最適料金において参加Lのproviderへの寄与は正。flatでは `a(a/2-c)>0`、meteredでは `F+(p-c)q_L>0`。正の測度のLが不参加なら、Fを十分小さく下げて全Lの参加を確保する逸脱が有利になる。従ってpreferred equilibriumの参加を、恣意的なtie-breakingで支える必要はない。H-onlyでHが無差別な場合にも、正の利潤を実現するには同様の問題を確認する。

**両タイプが無差別。** baselineでは `p<a_H`で `S_H>S_L`なので同一正数量料金で両タイプが同時にゼロレントとはならない。`p>=a_H,F=0`のzero-usageは可能だがstrict Rでは最適でない。

**導入の無差別。** uniform cutoff上の個々の利用者は導入／非導入を変えられる。ただし測度ゼロであり、providerのbest responseを変えない。一般分布にatomを加えるとこの議論は使えないが、凍結baselineはatomを許していない。

**architectureの等利潤。** `mu=mu_M`ならregular outcomeは `h=h_M,rho=1`、`mu=mu_F`なら `h=h_F,rho=0`。providerだけを見れば混合可能でも、正則固定点の整合性により任意のrhoが均衡になるわけではない。歴史的記録の「boundary tie sets」はprovider best-response setという意味なら正しいが、aggregate equilibriumの連続体を意味するなら未証明である。現稿は境界を除外しておりheadlineへの影響はない。

**active-setの等利潤。** §10.3では料金行動がprovider payoffを変えずHの期待レントを変える。本監査は両行動を保持して別均衡を構成した。これは単なるoff-path strategy multiplicityとは異なる。

**判定：** strict R内の未処理の実質的多重均衡という攻撃はFALSE POSITIVE / NO ISSUE。境界記録の意味はMINORな明確化対象。outside-Rのarchitecture内混合は実在するが、凍結範囲外である。

## 12. Mixed-equilibrium existence and uniqueness audit

strict R内で `Phi`は連続かつ狭義増加。`mu_M<mu<mu_F`なら中間値の定理で一意な `h* in (h_M,h_F)`があり、`Phi(h*)=mu`。

\[
\rho^*=\frac{b_H+R_F-K_Hh^*}{d p(h^*)}.
\]

`h*<h_F`から分子は正。`h*>h_M`と `g'<0`から `g(h*)<0`、従って分子は `dp(h*)`より小さい。よって `0<rho*<1`。

混合確率から導入量を定める式

\[
K_Hh=b_H+R_F-\rho dp(h)
\]

の微分は

\[
\frac{dh}{d\rho}=-\frac{dp(h)}{K_H+\rho d p'(h)}<0.
\]

これは原稿の混合結果の存在・一意性を支える経済部分であり、Leanの無差別条件だけで代替できない。さらに§9で他のactive setを排除済みなので、同じstrict baseline R内の別のaggregate outcomeを取り逃していない。

off-path継続は§7の大域包絡から各状態に選べる。両タイプともゼロの履歴ではno-serviceを選べる。一方のみ正の履歴ではそのタイプの一部料金／二部料金最大を選べる。atomlessな個別の導入逸脱が総量を変えないことと、任意の履歴で継続戦略を定義できることは別に確認した。

## 13. Quantifier / functional-form red team

### 13.1 Abstract sufficient condition

`x_M<x_F`かつ `Psi'>0`から閾値分離を得る部分は**order preservationの即時系**である。数学的には正しいが、一般的な経済結果を追加したことにはならない。economic contentは、primitiveからレントの順序、導入固定点、大域料金gainの単調性を証明する部分にある。

現稿はarbitrary concave utilityを主張しておらず、その方向のfalse-theorem attackはNO ISSUE。ただし抽象lemmaを「quadraticを超えた一般理論の確立」と売ることは認められない。

### 13.2 CDF regression: exact economic failure

既存sqrt例は `G(k/8)=sqrt(k/8)` と解釈される。両タイプ式による `h_F=sqrt(5/8)=0.7905694150`では

\[
H_F-B_F=\frac92\sqrt{5/8}-\frac{16}{5}>0.
\]

従ってそのflat continuationでHのレントを `9/2`と置くことは誤り。実際の最適flat料金はH-onlyでHレントゼロ。

| 対象 | 値 |
|---|---:|
| branch metered fixed point | 0.6657510130 |
| branch flat state | 0.7905694150 |
| 上記metered状態の大域gain | 1.5498201422 |
| 上記flat状態の大域gain | 1.4247622748 |
| 無効な両タイプflat比較からのgain | 1.7823246425 |

最後の二つの大域gainの大小が逆転しても、「真の二つの均衡閾値が逆転した」とは言わない。一方のstateが真のflat-induced stateではないためである。

さらに `mu=17/10`で、§10の `h_B=32/45`においてflat料金を混合し、両タイプ料金の確率を

\[
\lambda=\frac{8(32/45)^2-1/2}{9/2}=\frac{14359}{18225}
\]

にすると、Hの導入条件 `h=sqrt((b_H+lambda R_F)/8)`が厳密に成立する。providerは `17/10>250/153`なのでflatを厳密に好む。従ってこのロバストネス例には、branch計算が示唆する混合architecture以外の整合的な解法がある。

分類はB2のとおり。**baseline T1–T3を否定せず、CDF例の経済的認証を否定する。**

### 13.3 Independently chosen nonquadratic utility

既存の `r=3,4` を再実行せず、以下を選んだ。

\[
v_j(q)=a_j(1-e^{-q})-\epsilon q,\quad \epsilon=1.
\]

厳密凹、有限のsatiationあり。flatで数量が無限になるlog utilityのような不適格な反例を使っていない。

\[
q_j(p)=\left[\log\frac{a_j}{p+\epsilon}\right]_+,\quad
S_j(p)=a_j-t-t\log(a_j/t),\ t=p+\epsilon<a_j.
\]

両タイプ供給のFOCは

\[
B'(p)=h\log(a_H/a_L)-\frac{(l+h)(p-c)}{p+\epsilon},
\quad B''(p)=-\frac{(l+h)(c+\epsilon)}{(p+\epsilon)^2}<0.
\]

`z=h log(a_H/a_L)/(l+h)<1`なら `p=(c+epsilon z)/(1-z)`、ただしchokeとactive setの比較が必要。H-onlyの最大は引き続き `p=c`である。

独立の全料金再最適化で `a_L=8,a_H=10,c=.2,l=.8,b_H=.2,K_H=8`を検査した。

- `h_M=0.2397130487 < h_F=0.2471070561`
- 両architectureでBが大域最適。
- tested intervalのgainは `0.0319400699`から `0.0325047735`に増加。

数値例としてPASS。任意の非二次効用を証明したとはしない。

### 13.4 Adversarial heterogeneity / curvature reversal

追加攻撃としてタイプごとの曲率を変えた厳密凹効用を調べた。

\[
v_L(q)=4q-q^2/2,\quad v_H(q)=12q-4q^2.
\]

`c=1,l=4/5,h=3/10`でflatはB・`F=8`・Hレント1。meteredの大域B最適は `p=7/46`でHレントが約1.3703036に**増える**。独立コードに厳密分数の証明用計算を保持した。

ただし、このHは高い総支払意思額のタイプであり、flat利用量は `q_H=3/2<q_L=4`。よって凍結baselineや「Hがすべての価格で高利用」の仮定に対する反例ではない。示すのは、**凹性と総支払意思額の順序だけではレント減少は保証されない**という限定的な事実。仮定違反を隠して反例と呼ばない。

### 13.5 Exogenous integration benchmark

導入量を固定すれば同じ大域gainに対する一つのthresholdに戻る。strict Rでのcollapse系は正しい。ただし「導入の内生性だけがgapの十分条件」とは言えない。architecture依存性、レントの残存、μによる非凸な料金方式選択が必要。`mu=0`では正則branchのmeteringが優位でgap領域に入らない。

## 14. Welfare-selection audit

### 14.1 First best

直接数量を選ぶplannerは `q_j=a_j-c`を選び、導入cutoffは `b_j+(a_j-c)²/2`。導入比率はそのcutoff/Kを `[0,1]`に切り詰める。plannerは課金のためにmeteringをactivateしない。このchoice setを費用μを含むtariff実装plannerと混同しない。

### 14.2 Fixed installed base

\[
\omega_j(p)=v_j(q_j(p))-cq_j(p)=\frac{(a_j-c)^2-(p-c)^2}{2}.
\]

従って

\[
W_M-W_F=\frac n2\left[c^2-d^2(h/n)^2\right]-\mu.
\]

`mu_P-mu_W=dh p*>0`を独立に得る。μの符号制約にも注意し、`mu_W<0`なら非負のμでmeteringを好む社会領域は空。これは固定導入量・provider最適料金同士の比較であり、planner最適料金の比較ではない。

### 14.3 Endogenous integration: independent sign reversal

`a_L=4,a_H=5,c=1,b_L=16/5,K_L=4,b_H=1/2,mu=0`を固定する。

| K_H | h_M | h_F | W_M(l,h_M)-W_F(l,h_F) |
|---:|---:|---:|---:|
| 8 | 0.4547003073 | 0.625 | −0.0819480028 |
| 160 | 0.0248119876 | 0.03125 | +0.3894029191 |

双方ともstrict R。計算は各typeの `v(q)-cq`と導入費用の積分から行い、tariff transfersを加算していない。μを小さな正値にしてもこの符号差は残る。

これはarchitecture commitment下の二つの異なるゲームの比較であり、同一の非コミットメントゲームで自由に均衡を選んだ比較ではない。現稿の区別は正しい。

### 14.4 Mixed welfare and selection

正則混合結果では導入費用は一回だけ発生するため、

\[
W_{mix}=(1-\rho^*)W_F(l,h^*)+\rho^*W_M(l,h^*)
\]

は正しい。双方に同じ導入費用を含めても重みの和が1なので二重計上にならない。

§10のflat料金混合ではarchitectureは一定でも供給されるLの測度がランダムなので、単に `W_F(l,h)` のB式を使えない。既に導入したLの費用はH-onlyが選ばれても発生済み。一般CDFでは積分費用自体も `K_H h²/2`から変わる。例えばsqrt CDFなら `K_H h³/3`。outside-Rに現在の厚生式を拡張してはいけない。

**C2**：厚生の移転会計・first best混同攻撃 → FALSE POSITIVE / NO ISSUE。証拠は上記恒等式と独立符号反転。現稿で回答可能。修正不要。Stage 7のbaseline認証は維持。Certification regression: NO。

## 15. Prior-art absorption test

### 15.1 Search scope and source quality

2026-09-12に二つのweb search系統を用い、指定された全著者群に加え、nonlinear pricing、subscription/pay-per-use、dynamic adoption、hold-up、platform commitment、business-model choice、cloud contracts、2024–2026 LLM pricingを検索した。以下は一次資料に基づく比較である。全文を取得できなかった論文について「全定理を確認した」とはしない。

| 研究 | 確認水準・一次資料 | 脅威と判定 |
|---|---|---|
| Sundararajan (2004), Nonlinear Pricing of Information Goods | 著者公開稿全文：[NYU](https://oz.stern.nyu.edu/papers/nlp0703.pdf) | 固定費・従量料金・取引費用のstatic基礎は既知。採用は料金メニューに応じたstatic選択で、先行するsunk integrationから事後architecture選択への本稿のゲームそのものとは異なる。 |
| Muthers & Wismer, Why Do Platforms Charge Proportional Fees? | [publisher](https://doi.org/10.1515/rne-2023-0020)。公開本文の取得は不安定。publisher索引でstage 1 tariff / 後続entryの記述を確認 | tariff form、sunk seller participation、hold-up mitigationは強い重複。全ゲームの完全包含を認定するだけの全文照合は本監査ではしていない。 |
| Penmetsa, Gal-Or & May (2015) | [publisher abstract](https://journals.sagepub.com/doi/abs/10.1111/poms.12317) | subscription histories、strategic adoption、commitmentの価値は既知。全文access制限あり。本文全命題の非包含を保証しない。 |
| Ladas, Kavadias & Loch (2022) | [Cambridge accepted-manuscript metadata / abstract](https://www.repository.cam.ac.uk/items/15352bb6-42d6-4615-aa2f-f608a8499097)、[publisher](https://doi.org/10.1287/mnsc.2021.4125) | product selling対PPUのduopolyとbusiness-model differentiation。mixed business modelの新規性は主張できない。取得された別bitstreamは別論文だったため、内容照合に使わなかった。 |
| Wang & Hu (2014), Committed Versus Contingent Pricing Under Competition | [publisher abstract](https://journals.sagepub.com/doi/abs/10.1111/poms.12202) | 対称primitiveでも非対称なpricing choiceと一意なmixed strategy equilibriumが生じる。pricing-regime mixing自体は既知。需要不確実性・容量・duopolyが中心で、本稿と同じゲームではない。 |
| Bergemann, Bonatti & Smolin (2026), Menu Pricing of Large Language Models | [Cowles 2502全文](https://cowles.yale.edu/sites/default/files/2026-03/d2502.pdf) | 2025年版の後続。多次元task価値、token budget、committed-spend、menu実装を扱う。現在の引用版だけではfrontier照合が古い。AI料金の設計自体を新規性にできない。 |
| Bergemann & Wang (2025) | [arXiv全文](https://arxiv.org/html/2502.08022v1) | demand signalに基づく事前契約とsequential screening。buyer commitment costとspot marketも扱う。事後に契約体系を選び直す本稿のcommitment failureとはtimingが異なる。 |
| Bhaskaran, Erat & Mukherjee (2026) | [publisher本文](https://journals.sagepub.com/doi/full/10.1177/10591478261454768) | 前払いと利用時点の分離、mental accounting、serving cost、quality/two-part extensions。prepaymentの行動効果であり、sunk integrationからproviderのex-post architecture誘因への本稿の機構ではない。 |
| Min & Ryu (2025), Price Discrimination, Two-Part Tariff, and Hold-Up | [publisher全文](https://onlinelibrary.wiley.com/doi/full/10.1111/manc.70001) | 事前投資→事後二部料金、匿名性によるレント残存、投資と厚生の相反が直接重なる。§15.2のclosest-paper test対象。 |
| Bichuch & Yaish (2026), Freemium Is All You Need | repoのarXiv識別子2608.00823への取得を試行したが本文取得不能 | 今回の独立監査では内容・最新版を再認証しない。過去のsource-verification表をそのまま証拠にしない。 |

この検索は「関連研究が存在しない」ことの証明ではない。特に全文未取得の論文についてwhole-game novelty PASSを与えない。Min–Ryuは完全なモデル本文を読めたため、もっとも直接的な比較に用いた。

### 15.2 Whole-game absorption test — Min & Ryu

本監査で最も危険なclosest paperとして選ぶ理由は、単にplatform一般に近いからではなく、**投資後に供給者が二部料金を再最適化し、共通料金が残すレントが先行投資に影響する**という経済構造が直接重なるため。

| 本稿の対象 | Min–Ryuへの翻訳候補 | 保存できるか |
|---|---|---|
| integration | downstreamの `I/NI` | sunk decisionという役割は対応 |
| installed composition `(l,h)` | 実現したcost pair `(c_i,c_j)` | stateという役割は対応、連続的な内生測度とは異なる |
| anonymous `(F,p)` | uniform `(F,w)` | rent-extraction制約は近い |
| flat対meteredの事後選択 | discriminatory対uniformの比較 | **不可**：後者は制度的制約の比較であり、μを払う事後architecture actionではない |
| `mu_M,mu_F` | investment threshold `I_u` | **不可**：意思決定主体・費用・閾値の意味が異なる |
| `rho*` | investment / tariff選択 | 本稿の二つの条件を同時に保存する対応なし |

同論文の§2–3では投資、供給契約、下流価格競争を解き、価格差別の有無を比較する。`I_u`にμを単に代入しても、本稿のprovider best responseとatomless導入条件は得られない。対応を成立させるには新しい事後architecture actionとactivation costを追加する必要があり、notation変更ではない。

**判定：そのままのwhole-game absorptionは成立しない。** ただし、これは本稿の増分が大きいことを意味しない。残存レント・投資・厚生の主要直観は近く、本稿の独自部分は二択architectureの自己整合性に限定される。

### 15.3 Institution: FACT / SUGGESTIVE / MODEL INTERPRETATION

| 区分 | 命題 | 確認・限界 |
|---|---|---|
| FACT | OpenAIにはBusinessのseat pricing、Enterpriseのcustom pricing・credit/token型の選択肢がある | [公式pricing](https://openai.com/business/pricing/)で確認。具体的な単価は論文の機構を検証しないので記載しない。 |
| FACT | Businessではincluded limitsと追加credits、Enterpriseでは契約のpool・overage等がある | [公式flexible pricing](https://help.openai.com/en/articles/11487671-flexible-pricing-for-the-enterprise-edu-and-business-plans)。全利用量でp=0のflatとは同一でない。 |
| FACT | APIの課金表はusage関連の料金を掲載している | [公式API pricing](https://developers.openai.com/api/docs/pricing)。複数token種類・機能の単位を一つのqに集約するのはモデル化。 |
| FACT | AWS Savings Plansは時間あたりの支出コミットメントに対応し、超過にはOn-Demand料金が適用される | [公式FAQ](https://aws.amazon.com/savingsplans/faqs/)。無制限flat subscriptionではない。 |
| SUGGESTIVE | workflow integrationに将来回収を期待する組織固有費用がある | [OpenAI enterprise report](https://openai.com/business/guides-and-resources/the-state-of-enterprise-ai-2025-report/)は利用・統合の実態を示唆するが、kや非回収性を識別しない。 |
| MODEL INTERPRETATION | 導入構成がproviderの次期architecture変更を誘発する | 今回確認した料金表からは立証不能。原稿も理論機構と述べている。 |
| MODEL INTERPRETATION | μは正で固定の追加的real cost | 公式資料から同定されない。既存計量機能のsunk cost、transfer、procurement aversionとは区別が必要。 |

料金制度の存在→導入が料金制度を変えた、という推論は採用しない。実証的な因果主張としてはUNVERIFIED、理論解釈としては明示されている。

## 16. Lean / formal-verification fidelity audit

ソースは `formal/DynamicTariffFormal.lean`。freezeとmanuscript commit間で同ソース・freeze registersに差分はなかった。

| Lean theorem | 供給された仮定 | 実際に証明すること | 証明しないこと |
|---|---|---|---|
| `threshold_separation` | `StrictMono Psi`, `hM<hF` | `Psi hM<Psi hF` | primitiveからの順序・大域gain |
| `strict_gap_reverses_pure_responses` | 二つのstrict inequalities | それらをpreferred predicatesとして束ねる | 利潤最大化・均衡非存在 |
| `antitone_fixedPoint_unique` | 全実数上のAntitoneと二固定点 | at most one fixed point | existence、経済写像がAntitoneであること |
| `fixedPoint_below_flat_state` | Antitone、fixed point、crossing | 状態の順序 | 存在・内部性・active set |
| `mixed_state_unique` | `StrictAnti hOfRho`, `StrictMono Psi`、二解 | rhoの一致 | 混合均衡の存在、確率範囲 |
| `baseline_phi_derivative_positive` | `c,d,l>0,h>=0` | 表示された有理式の正値性 | その式がPhiの導関数であること |
| `hOnly_scope_counterexample` | 固定された有理数 | 差23/10の算術 | 一般的なactive-set比較 |

ソースに `sorry` / `admit` / project-specific `axiom` / unsafe proofは見つからなかった。`#print axioms`は記述されている。ただし本環境にはlakeがなく、今回kernel buildや依存ライブラリ由来のaxiom出力を再実行していない。既存certificateのgreen CIを今回の独立数学証拠としては用いない。

また `StrictMono Psi` 等は全実数上の仮定であり、baselineで必要なのは経済区間上の性質。実際のbaseline関数をそのままグローバルな仮定へ代入した完全な形式証明は存在しない。必要なら区間版または延長のadapterが必要だが、現在のsourceは条件付きのskeletonであると明示している。

**F1**

- Attack → Lean PASSをcomplete economic theoremと誤認していないか。
- Severity → FALSE POSITIVE / NO ISSUE（conditional scope）。全実数domain adapterの不在はMINORな説明対象。
- Exact evidence → 上記signatures、`sections/05_robustness.tex`末尾、formal certificateの明示的non-formalized list。
- Mathematical/economic consequence → 本監査のCDF active-set失敗はLeanの仮定の外側にあり、Lean PASSと両立する。
- Can the paper answer now? → YES、限定の記述は適切。
- Required fix → 新しい経済認証とLeanのconditional certificateを混同しない。encoded statementを変える場合のみ再build / fidelity audit。
- Earliest affected stage → Stage 7.5A formal gate（変更時のみ）。
- Certification regression? → NO、Lean定理を反証したわけではない。

## 17. Evidence ledger for all material PASS findings

| PASS claim | 実行したattack | 独立証拠 | 残る限定 |
|---|---|---|---|
| qとS | constrained utility maximization | §7.1、直接utility evaluator | quadratic baseline |
| p*とF* | SOC、fixed-fee cells、境界 | §7.2–7.4の平方完成・包絡 | strict Rでinterior B |
| 大域continuation | H-only / no-service / zero F | 全active-set envelope、direct optimizerとの比較 | 数値探索自体は一般証明でない |
| Rの非空性 | 上端のstrict margins | 31/80、3533/2280 | 他のparameter全域に拡張しない |
| Phi_h>0 | 利潤差から再導出 | §7.6 | active set切替後は使わない |
| 0<h_M<h_F | 正根・endpoint・monotonicity | §8、utility-rentからのroot solve | distributionとRが必要 |
| no pure architecture in strict R gap | 二候補逸脱＋別状態排除 | §8–9 | pure architectureとpure tariff actionを区別 |
| mixed outcome existence / uniqueness | probability bounds、state response | §12 | off-path strategiesの一意性ではない |
| payoff-indifferent参加で追加結果なし | Fのepsilon逸脱 | §11 | strictな供給利潤が必要 |
| fixed-base W1 | transfersを除いて再集計 | §14.2 | policy theoremではない |
| endogenous welfare reversal | 独立parameter二例 | §14.3、JSON | architecture commitment比較 |
| 非二次の生存例 | exponential utilityから再最適化 | §13.3、JSON | 数値例、一様H cost |
| formal proseのscope | signatures対本文 | §16 | fresh kernel buildは未実行 |
| 全ゲーム直接包含ではない | Min–Ryuのtiming/action対応 | §15.2 | すべての既存研究からの新規性証明ではない |

数値solverは失敗・NaNをunprofitable deviationとして扱わず例外にする。独立実装と解析有限候補の比較誤差は約 `1.78e-15`。探索時に不適切な仮定を使った結果をPASSに混ぜていない。curvature反転はhigh-use ordering外、sqrt例はR外と分類した。

## 18. Certification-regression ledger

| ID | 過去認証 | 新しい証拠 | 不足check | rollback |
|---|---|---|---|---|
| CR-01 | Stage 7.5A §3のsqrt CDFをstate-orderingの経済的robustness例として記録、Stage 8に持越し | `h_F=sqrt(5/8)`でH-only flatが+0.3575623677。実際の大域gainはbranch式と異なり、pure-flat / fee-mixed equilibriumを構成可能 | distributionを変えるたび、全導入区間のglobal continuationと参加集合を再確認する。仮定されたrent-mapのチェックとequilibrium validationを分離する | **Stage 7.5A**、その後Stage 8再確認 |

これはStage 4のuniform baselineを無効にする回帰ではない。Stage 7のwelfare accounting、conditional Lean theoremを無効にする回帰でもない。過去記録を削除・書換えず、訂正記録と反例を追加すべきである。

## 19. Consolidated severity table

| ID | 発見／攻撃 | severity | 状態 |
|---|---|---|---|
| B2 / CR-01 | sqrt CDFのactive-set認証失敗 | MAJOR BUT FIXABLE | 確定。Stage 7.5Aをreopen |
| A1 | closest-paper比較とfrontier更新不足 | MAJOR BUT FIXABLE | 確定した比較不足。完全包含は未立証 |
| B1 | Rとalternative-equilibrium排除の原稿説明不足 | MAJOR BUT FIXABLE | 独立論証で回答可能。baseline反例なし |
| C1 | μとtask契約単位の制度的根拠 | MAJOR BUT FIXABLE | モデル解釈として明示されるが説得力が弱い |
| D1 | Model Improvementの題名 | MINOR | 本文は条件付きだが期待とのずれ |
| I1 | architecture threshold境界のtie set説明 | MINOR | 任意の混合が均衡とは限らない |
| F1 | Leanの過剰な経済証明主張 | FALSE POSITIVE / NO ISSUE | 限定は明示。source-level fidelityのみ今回監査 |
| M1 | strict R内のp*、Phi、h順序、混合一意性の誤り | FALSE POSITIVE / NO ISSUE | 独立解析・大域比較を通過 |
| M2 | strict R内のH-only等の別均衡 | FALSE POSITIVE / NO ISSUE | 別状態の排除論証を構成 |
| C2 | first best混同・移転二重計上 | FALSE POSITIVE / NO ISSUE | 三benchmark区別と独立符号反転が成立 |
| S1 | outside-Rのpure-flat / fee-mixed equilibrium | FALSE POSITIVE / NO ISSUEとしてbaselineへの反例を棄却 | 実在するscope guard。CR-01の証拠としてはmaterial |
| N1 | Min–Ryuに主定理がそのまま包含 | FALSE POSITIVE / NO ISSUE（直接包含攻撃） | timing / actionが保存できない |

**FATALの認定：なし。** 「FATALなし」と「現在の認証のまま次stageへ進める」は同義ではない。CR-01はworkflow上、先行認証の訂正・再確認を要する。

## 20. Exact required repairs

1. **Stage 7.5Aの証拠分類を訂正する。** sqrt例はabstract antitone mapの算術チェックとしてなら残せるが、実際の料金ゲームの頑健性を支持する例としては撤回し、active-set counterexampleとして保持する。
2. **同stageの各例にglobalityを付す。** CDFまたはutility変更後の導入区間、両architectureの全料金最大、参加集合、strict marginsを記録する。失敗例を捨てたり値をこっそり変更したりしない。
3. **§10.3 / §13.2の料金額混合をnegative evidenceに残す。** provider等利潤でも他playerのレントが変わる行動を削除しないcheckを追加する。これは新しいextensionを論文に足せという指示ではない。
4. **Rの経済的制約と別均衡排除を説明する。** §7.5 / §9の展開により凍結された条件を読者が検証できるようにする。新仮定が必要ならStage 4/4Aに戻すが、今回のbaselineにはその必要性は確認されなかった。
5. **novelty ledgerを更新する。** Min–Ryu、Wang–Hu、Ladas、およびBBS 2026版との比較を明示。全文未取得の重要候補はunresolvedのまま記録し、抽象lemmaの正しさをnoveltyに数えない。
6. **制度説明と題名を整合する。** 料金併存はFACT、integration→repricingの機構はMODEL INTERPRETATION。μの存在単位と匿名task契約の限界を明記。quality拡張を足して問題を回避しない。
7. **再認証後にStage 8を再確認する。** 条件付きLean source自体は本発見で偽にならない。証明statementを変えた場合にだけformal certificateを更新・再buildし、経済的認証と区別する。

本監査は上記修正を実装していない。既存production scriptの欠陥を指摘する独立回帰コードと報告だけを追加した。

## 21. Earliest rollback stage, if any

**Stage 7.5A — Generality / Quantifier Red-Team。**

理由：今回確定した不成立は、そのstageで導入されたsqrt CDFロバストネスのeconomic validationである。元のuniform baselineの正則領域に反例があるわけではないため、Stage 4へ全面rollbackする理由はない。

再確認の経路は、`Stage 7.5A correction / recertification → Stage 8 confirmation → Stage 10 bounded exposition → Stage 11再判定`。noveltyの更新はStage 6の比較ledgerを参照して行う。新しい制度・非線形料金・分布一般化を研究し直す場合は、その変更の最初の科学stageへ別途戻す。

## 22. Final Stage-11 verdict

**REOPEN EARLIER STAGE / NO-GO**

baselineのpure-regime gapは、strict Rでは独立監査に耐えた。破壊できたのは、CDFロバストネスを認証済みとする証拠の一部と、R外へ結果を拡張した場合のarchitecture非存在の解釈である。認証回帰を処理せず、現在の全パッケージをjournal positioningへ進めることは認めない。

**IJIO査読判断：Reject。**

Reject。正則領域内の閾値分離と混合均衡は独立再導出に耐えており、中心定理が誤りだとは判断しない。しかし、一般CDFのロバストネス例が大域的な料金最適性を満たしておらず、認証済みという説明と経済的な検証範囲が一致していない。領域の直外では料金方式を変えず料金額だけを混合する均衡が生じるため、境界の扱いは実質的である。さらに、最新の二部料金・ホールドアップ研究との比較が不足し、モデル改善を題名に掲げる割に改善過程はモデル化されていない。現状では、正しい限定的命題をIJIOの独立した理論貢献として評価するための根拠が足りない。
